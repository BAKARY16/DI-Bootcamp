"""
main.py
-------
Point d'entrée principal du projet AI Content Generator.
Lance le pipeline complet : génération → traitement → analyse → recommandations → visualisations.
"""

import os
import sys

# Ajouter src/ au chemin Python
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from data_generator import generate_users, save_raw_data
from data_processor  import process
from analyzer        import analyze
from recommender     import RecommendationEngine
from visualizer      import generate_all


def main():
    print("=" * 55)
    print("  AI Content Generator — Pipeline complet")
    print("=" * 55)

    # Étape 1 : Génération des données
    print("\n[1/5] Génération des profils utilisateurs...")
    df_raw = generate_users(n_users=500)
    save_raw_data(df_raw, path="data/raw/users_raw.csv")

    # Étape 2 : Traitement et nettoyage
    print("\n[2/5] Traitement et nettoyage des données...")
    df = process(
        raw_path="data/raw/users_raw.csv",
        clean_path="data/processed/users_clean.csv"
    )

    # Étape 3 : Analyse statistique
    print("\n[3/5] Analyse statistique (SciPy)...")
    stats_results = analyze(df)

    # Étape 4 : Recommandations
    print("\n[4/5] Génération des recommandations...")
    engine = RecommendationEngine(df)

    # Démonstration sur 3 utilisateurs
    for user in engine.profiles[:3]:
        recs = engine.recommend(user, top_n=3)
        print(f"\n  → {user.name} ({user.interests})")
        for r in recs:
            print(f"     [{r['score']:.0%}] {r['titre']}")

    # Étape 5 : Visualisations
    print("\n[5/5] Génération des graphiques...")
    generate_all(df)

    print("\n" + "=" * 55)
    print("  Pipeline terminé avec succès !")
    print("  Graphiques disponibles dans : backend/outputs/")
    print("=" * 55)


if __name__ == "__main__":
    main()
