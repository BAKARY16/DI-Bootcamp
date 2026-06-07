import json
import os
import socketserver
import webbrowser
from http.server import SimpleHTTPRequestHandler

from data_generation import generate_users, activity_matrix
from recommender import ContentRecommender
from recommender_v2 import User, Content, RecommendationEngine
from statistical_analysis import model_interest_distribution, simulate_preference_distribution
from visualize import plot_interest_distribution, plot_activity_heatmap, plot_recommendations_by_segment

CONTENT_CATALOG = {
    "fitness": [
        "Daily 20-min HIIT",
        "Beginner running plan",
        "Yoga for flexibility"
    ],
    "technology": [
        "Top AI blogs",
        "Intro to machine learning playlist",
        "Gadget reviews weekly"
    ],
    "music": [
        "Top rock playlist",
        "Indie discovery list",
        "Classical focus album"
    ],
    "books": [
        "Sci-fi recommendations",
        "Business book list",
        "Poetry picks"
    ],
    "cooking": [
        "Quick healthy recipes",
        "Baking 101 series",
        "Vegetarian meal plan"
    ],
    "travel": [
        "Weekend getaway ideas",
        "Budget travel tips",
        "Cultural guides"
    ]
}


def build_dashboard_data():
    base_dir = os.path.dirname(__file__)
    frontend_dir = os.path.join(base_dir, "frontend")
    os.makedirs(frontend_dir, exist_ok=True)

    df = generate_users(120, seed=42)
    df = df.drop_duplicates(subset=["name"]).reset_index(drop=True)

    plot_interest_distribution(df, out_path=os.path.join(frontend_dir, "interest_distribution.png"))
    mat = activity_matrix(df)
    plot_activity_heatmap(mat, out_path=os.path.join(frontend_dir, "activity_heatmap.png"))

    from scipy import stats

    all_interests = [interest for interests in df["interests"] for interest in interests]
    interest_counts = {interest: all_interests.count(interest) for interest in CONTENT_CATALOG.keys()}
    expected = [sum(interest_counts.values()) / len(interest_counts)] * len(interest_counts)
    chi2, p_value = stats.chisquare(list(interest_counts.values()), f_exp=expected)

    hourly_activity = mat.sum(axis=1).astype(int).tolist()
    hours = list(map(str, mat.index.tolist()))
    category_counts = mat.sum(axis=0).astype(int)
    category_labels = category_counts.index.tolist()
    category_values = category_counts.tolist()
    top_hours = sorted([(int(hour), int(count)) for hour, count in zip(mat.index.tolist(), hourly_activity)], key=lambda x: x[1], reverse=True)[:5]

    rec = ContentRecommender(CONTENT_CATALOG)
    sample_user = df.iloc[0].to_dict()
    suggestions = rec.recommend(sample_user, n=5)

    other_profiles = [row.to_dict() for _, row in df.sample(10, random_state=1).iterrows()]
    similar_suggestions = rec.recommend_by_similarity(sample_user, other_profiles, n=3)

    to_do = [
        {"task": "Générer un jeu de données synthétique", "done": True},
        {"task": "Prétraiter les données avec Pandas", "done": True},
        {"task": "Analyser les intérêts et l'activité", "done": True},
        {"task": "Utiliser SciPy pour un test statistique", "done": True},
        {"task": "Modéliser les distributions probabilistes", "done": True},
        {"task": "Afficher des graphiques Matplotlib/Seaborn", "done": True},
        {"task": "Créer un système de recommandation OOP", "done": True},
        {"task": "Analyser la similarité entre utilisateurs", "done": True}
    ]

    # Modélisation probabiliste des préférences
    interest_dist = model_interest_distribution(df, list(CONTENT_CATALOG.keys()))
    simulated = simulate_preference_distribution(interest_dist, n_simulations=100)

    # Créer les objets User pour analyse
    all_users = [User(row['name'], row['age'], row['interests'], row['activity_log']) 
                 for _, row in df.iterrows()]

    # Créer le moteur de recommandation avec classes
    content_catalog_v2 = {
        category: [Content(title, category) for title in titles]
        for category, titles in CONTENT_CATALOG.items()
    }
    engine = RecommendationEngine(content_catalog_v2)

    # Obtenir les recommandations par segment
    segment_recs = engine.recommend_by_segment(all_users, segment_key='age')
    plot_recommendations_by_segment(segment_recs, out_path=os.path.join(frontend_dir, "recommendations_by_segment.png"))

    data = {
        "summary": {
            "users": int(df.shape[0]),
            "total_activities": int(df["activity_log"].apply(len).sum()),
            "interest_counts": interest_counts,
            "chi2": float(chi2),
            "p_value": float(p_value)
        },
        "sample_user": {
            "name": sample_user["name"],
            "age": int(sample_user["age"]),
            "interests": sample_user["interests"],
            "activity_log": sample_user["activity_log"]
        },
        "suggestions": suggestions,
        "similar_suggestions": similar_suggestions,
        "interest_labels": list(interest_counts.keys()),
        "interest_values": list(interest_counts.values()),
        "hours": hours,
        "hourly_activity": hourly_activity,
        "category_labels": category_labels,
        "category_values": category_values,
        "top_interests": sorted(interest_counts.items(), key=lambda item: item[1], reverse=True),
        "top_hours": top_hours,
        "probabilistic_analysis": {interest: {
            'probability': float(params['probability']),
            'count': params['count']
        } for interest, params in interest_dist.items()},
        "todo": to_do,
        "recent_users": [
            {
                "name": row["name"],
                "age": int(row["age"]),
                "interests": row["interests"],
                "activity_count": int(len(row["activity_log"]))
            }
            for _, row in df.head(8).iterrows()
        ]
    }

    with open(os.path.join(frontend_dir, "data.json"), "w", encoding="utf-8") as writer:
        json.dump(data, writer, indent=2, ensure_ascii=False)

    return frontend_dir


def run_server(port=8000):
    frontend_dir = build_dashboard_data()
    os.chdir(frontend_dir)
    url = f"http://localhost:{port}"
    print(f"Dashboard disponible sur {url}")
    print("Génération de data.json et des graphiques terminée.")
    webbrowser.open(url)

    handler = SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", port), handler) as httpd:
        httpd.serve_forever()


if __name__ == "__main__":
    run_server()
