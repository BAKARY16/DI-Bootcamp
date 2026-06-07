"""
api.py
------
API Flask simple qui expose les fonctionnalités du backend au frontend React.
Lance avec : python api.py
"""

import os
import sys
import json

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from flask import Flask, jsonify, request
from flask_cors import CORS

from data_generator import generate_users, save_raw_data
from data_processor  import process
from analyzer        import analyze
from recommender     import RecommendationEngine
from visualizer      import generate_all

app = Flask(__name__)
CORS(app)  # Autorise les requêtes du frontend React

# État global (chargé au démarrage si les données existent)
engine     = None
df         = None
stats_data = None


def load_or_generate():
    """Charge les données existantes ou les génère si absentes."""
    global engine, df, stats_data
    
    clean_path = "data/processed/users_clean.csv"
    raw_path   = "data/raw/users_raw.csv"
    
    if not os.path.exists(clean_path):
        print("[API] Données absentes, génération en cours...")
        df_raw = generate_users(500)
        save_raw_data(df_raw, raw_path)
        df = process(raw_path, clean_path)
    else:
        import pandas as pd
        df = process(raw_path, clean_path)
    
    stats_data = analyze(df)
    engine     = RecommendationEngine(df)
    print("[API] Prêt.")


@app.route("/api/status")
def status():
    return jsonify({"status": "ok", "users": len(df) if df is not None else 0})


@app.route("/api/users")
def get_users():
    """Retourne la liste paginée des utilisateurs."""
    page     = int(request.args.get("page", 1))
    per_page = int(request.args.get("per_page", 20))
    
    users = []
    for p in engine.profiles[(page-1)*per_page : page*per_page]:
        users.append({
            "user_id":      p.user_id,
            "name":         p.name,
            "age":          p.age,
            "interests":    p.interests,
            "activity_log": p.activity_log,
        })
    
    return jsonify({"users": users, "total": len(engine.profiles), "page": page})


@app.route("/api/recommend/<user_id>")
def recommend(user_id):
    """Retourne les recommandations pour un utilisateur donné."""
    top_n = int(request.args.get("top_n", 5))
    recs  = engine.recommend_by_id(user_id, top_n=top_n)
    return jsonify({"user_id": user_id, "recommendations": recs})


@app.route("/api/stats")
def get_stats():
    """Retourne les résultats de l'analyse statistique."""
    return jsonify(stats_data)


@app.route("/api/visualize")
def visualize():
    """Génère tous les graphiques et retourne leurs chemins."""
    paths = generate_all(df)
    return jsonify({"generated": paths})


if __name__ == "__main__":
    load_or_generate()
    app.run(debug=True, port=5000)
