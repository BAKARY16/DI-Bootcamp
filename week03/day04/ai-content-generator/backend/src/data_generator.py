"""
data_generator.py
-----------------
Génère un ensemble de données synthétiques de profils utilisateurs.
Utilise NumPy pour les valeurs aléatoires et Pandas pour structurer les données.
"""

import numpy as np
import pandas as pd
import json
import os

# Listes de données de base
NAMES = [
    "Alice Martin", "Bob Dupont", "Clara Ndiaye", "David Kouassi",
    "Emma Traoré", "Felix Bernard", "Grace Mbaye", "Hugo Lambert",
    "Iris Diallo", "Jules Fontaine", "Kara Sow", "Leo Petit",
    "Mia Dubois", "Nathan Bah", "Olivia Camara", "Paul Moreau"
]

INTERESTS = ["technologie", "fitness", "musique", "science", "voyage", "cuisine"]

ACTIVITY_TEMPLATES = {
    "technologie": [
        "watched AI talk", "read tech blog", "bought headphones",
        "watched coding tutorial", "downloaded dev app"
    ],
    "musique": [
        "listened to rock music", "created playlist", "bought concert ticket",
        "listened to jazz", "watched music video"
    ],
    "fitness": [
        "completed workout", "bought sports shoes", "tracked running",
        "watched fitness video", "bought protein powder"
    ],
    "science": [
        "read science article", "watched documentary", "subscribed to newsletter",
        "bought science book", "watched TED talk"
    ],
    "voyage": [
        "searched flights", "booked hotel", "read travel blog",
        "bought travel guide", "watched travel vlog"
    ],
    "cuisine": [
        "tried new recipe", "watched cooking video", "bought kitchen tool",
        "read food blog", "ordered ingredients online"
    ]
}


def generate_users(n_users: int = 500, seed: int = 42) -> pd.DataFrame:
    """
    Génère n_users profils utilisateurs synthétiques.
    
    Paramètres:
        n_users : nombre de profils à générer
        seed    : graine pour la reproductibilité
    
    Retourne:
        DataFrame avec colonnes: user_id, name, age, interests, activity_log
    """
    np.random.seed(seed)
    
    users = []
    
    for i in range(n_users):
        # Âge entre 18 et 65 ans
        age = int(np.random.randint(18, 66))
        
        # Nom aléatoire (avec répétition possible sur 500 users)
        name = NAMES[np.random.randint(0, len(NAMES))]
        name = f"{name.split()[0]} {name.split()[1]}_{i}"  # Rendre unique
        
        # Intérêts : entre 1 et 3 intérêts par utilisateur
        n_interests = np.random.randint(1, 4)
        user_interests = list(np.random.choice(INTERESTS, size=n_interests, replace=False))
        
        # Journal d'activité : 2 à 6 activités liées aux intérêts
        activity_log = []
        n_activities = np.random.randint(2, 7)
        for _ in range(n_activities):
            interest = np.random.choice(user_interests)
            activity = np.random.choice(ACTIVITY_TEMPLATES[interest])
            activity_log.append(activity)
        
        users.append({
            "user_id": f"U{i+1:04d}",
            "name": name,
            "age": age,
            "interests": json.dumps(user_interests),   # Stocké en JSON string
            "activity_log": json.dumps(activity_log),  # Stocké en JSON string
            "n_interests": n_interests,
            "n_activities": len(activity_log)
        })
    
    df = pd.DataFrame(users)
    return df


def save_raw_data(df: pd.DataFrame, path: str = "data/raw/users_raw.csv") -> None:
    """Sauvegarde les données brutes en CSV."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_csv(path, index=False)
    print(f"[OK] Données brutes sauvegardées : {path} ({len(df)} utilisateurs)")


if __name__ == "__main__":
    df = generate_users(n_users=500)
    save_raw_data(df)
    print(df.head(3).to_string())
