"""
recommender.py
--------------
Moteur de recommandation personnalisée basé sur les intérêts et activités.
Utilise la programmation orientée objet (OOP) et la similarité cosinus (SciPy).
"""

import pandas as pd
import numpy as np
from scipy.spatial.distance import cosine
import json


INTERESTS = ["technologie", "fitness", "musique", "science", "voyage", "cuisine"]

# Catalogue de contenu à recommander par catégorie
CONTENT_CATALOG = {
    "technologie": [
        {"titre": "Introduction au Machine Learning",        "type": "blog"},
        {"titre": "Les meilleurs outils pour développeurs",  "type": "article"},
        {"titre": "GPT-4 vs Gemini : comparatif complet",   "type": "article"},
        {"titre": "Apprendre Python en 30 jours",           "type": "cours"},
    ],
    "musique": [
        {"titre": "Playlist : Rock classique essentiels",    "type": "playlist"},
        {"titre": "Top 50 Jazz de cette semaine",            "type": "playlist"},
        {"titre": "Comment apprendre la guitare",            "type": "guide"},
        {"titre": "Les albums incontournables 2024",         "type": "article"},
    ],
    "fitness": [
        {"titre": "Programme HIIT 30 minutes",               "type": "programme"},
        {"titre": "Conseils nutrition pour sportifs",        "type": "article"},
        {"titre": "Top 10 équipements fitness à domicile",   "type": "guide"},
        {"titre": "Routine matinale en 15 minutes",          "type": "programme"},
    ],
    "science": [
        {"titre": "Les dernières découvertes en physique",   "type": "newsletter"},
        {"titre": "Comprendre la relativité générale",       "type": "article"},
        {"titre": "Top podcasts scientifiques 2024",         "type": "podcast"},
        {"titre": "CRISPR : révolution génétique",           "type": "article"},
    ],
    "voyage": [
        {"titre": "Top destinations été 2025",               "type": "guide"},
        {"titre": "Voyager avec un petit budget",            "type": "article"},
        {"titre": "Les plus beaux treks du monde",           "type": "guide"},
        {"titre": "Astuces pour éviter les arnaques",        "type": "article"},
    ],
    "cuisine": [
        {"titre": "Recette : Risotto crémeux parfait",       "type": "recette"},
        {"titre": "10 sauces à maîtriser absolument",        "type": "guide"},
        {"titre": "Cuisine végétarienne pour débutants",     "type": "cours"},
        {"titre": "Les épices du monde et leurs usages",     "type": "article"},
    ],
}


class UserProfile:
    """Représente un profil utilisateur avec ses préférences."""
    
    def __init__(self, user_id: str, name: str, age: int,
                 interests: list, activity_log: list):
        self.user_id     = user_id
        self.name        = name
        self.age         = age
        self.interests   = interests
        self.activity_log = activity_log
    
    def to_vector(self) -> np.ndarray:
        """
        Convertit le profil en vecteur numérique pour la similarité cosinus.
        Chaque dimension correspond à un intérêt (1 = a cet intérêt, 0 = non).
        """
        return np.array([1 if i in self.interests else 0 for i in INTERESTS],
                        dtype=float)
    
    def __repr__(self):
        return f"UserProfile({self.user_id}, {self.name}, intérêts={self.interests})"


class RecommendationEngine:
    """Moteur de recommandation basé sur les intérêts et les utilisateurs similaires."""
    
    def __init__(self, df: pd.DataFrame):
        self.df       = df
        self.profiles = self._build_profiles()
        print(f"[OK] Moteur initialisé avec {len(self.profiles)} profils")
    
    def _build_profiles(self) -> list:
        """Construit la liste des objets UserProfile depuis le DataFrame."""
        profiles = []
        for _, row in self.df.iterrows():
            interests    = row["interests"] if isinstance(row["interests"], list) else json.loads(row["interests"])
            activity_log = row["activity_log"] if isinstance(row["activity_log"], list) else json.loads(row["activity_log"])
            profiles.append(UserProfile(
                user_id=row["user_id"],
                name=row["name"],
                age=row["age"],
                interests=interests,
                activity_log=activity_log
            ))
        return profiles
    
    def find_similar_users(self, user: UserProfile, top_n: int = 3) -> list:
        """
        Trouve les utilisateurs les plus similaires via la similarité cosinus.
        Retourne les top_n utilisateurs les plus proches (excluant l'utilisateur lui-même).
        """
        user_vec = user.to_vector()
        similarities = []
        
        for other in self.profiles:
            if other.user_id == user.user_id:
                continue
            other_vec = other.to_vector()
            # Eviter la division par zéro (vecteur nul)
            if np.all(user_vec == 0) or np.all(other_vec == 0):
                sim = 0.0
            else:
                sim = 1 - cosine(user_vec, other_vec)  # 1 = identique, 0 = différent
            similarities.append((other, round(sim, 4)))
        
        # Trier par similarité décroissante
        similarities.sort(key=lambda x: -x[1])
        return similarities[:top_n]
    
    def recommend(self, user: UserProfile, top_n: int = 5) -> list:
        """
        Génère des recommandations personnalisées pour un utilisateur.
        Combine les intérêts directs + les comportements d'utilisateurs similaires.
        """
        recommendations = []
        seen_titles     = set()
        
        # 1. Recommandations basées sur les intérêts directs
        for interest in user.interests:
            if interest in CONTENT_CATALOG:
                for item in CONTENT_CATALOG[interest][:2]:  # 2 items par intérêt
                    if item["titre"] not in seen_titles:
                        recommendations.append({
                            "titre":  item["titre"],
                            "type":   item["type"],
                            "source": f"intérêt: {interest}",
                            "score":  0.90 + np.random.uniform(-0.05, 0.08)
                        })
                        seen_titles.add(item["titre"])
        
        # 2. Recommandations basées sur les utilisateurs similaires
        similar_users = self.find_similar_users(user, top_n=3)
        for similar_user, sim_score in similar_users:
            for interest in similar_user.interests:
                if interest not in user.interests and interest in CONTENT_CATALOG:
                    item = CONTENT_CATALOG[interest][0]
                    if item["titre"] not in seen_titles:
                        recommendations.append({
                            "titre":  item["titre"],
                            "type":   item["type"],
                            "source": f"utilisateur similaire (sim={sim_score})",
                            "score":  sim_score * 0.80
                        })
                        seen_titles.add(item["titre"])
        
        # Trier par score décroissant et retourner top_n
        recommendations.sort(key=lambda x: -x["score"])
        for r in recommendations:
            r["score"] = round(min(r["score"], 1.0), 2)
        
        return recommendations[:top_n]
    
    def recommend_by_id(self, user_id: str, top_n: int = 5) -> list:
        """Recommande pour un utilisateur identifié par son user_id."""
        user = next((p for p in self.profiles if p.user_id == user_id), None)
        if user is None:
            print(f"[ERREUR] Utilisateur {user_id} introuvable")
            return []
        return self.recommend(user, top_n)


if __name__ == "__main__":
    from data_processor import process
    df = process()
    engine = RecommendationEngine(df)
    
    # Test sur le premier utilisateur
    user = engine.profiles[0]
    print(f"\nRecommandations pour : {user.name} | Intérêts : {user.interests}")
    recs = engine.recommend(user)
    for i, r in enumerate(recs, 1):
        print(f"  {i}. [{r['score']:.0%}] {r['titre']} ({r['type']}) — {r['source']}")
