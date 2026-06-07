from Hachathon.custom_generator.data_generation import generate_users, activity_matrix
from Hachathon.custom_generator.recommender import ContentRecommender
from Hachathon.custom_generator.visualize import plot_interest_distribution, plot_activity_heatmap

CONTENT_CATALOG = {
    "fitness": [
        "Daily 20-min HIIT",
        "Beginner running plan",
        "Yoga for flexibility",
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
    "books": ["Sci-fi recommendations", "Business book list", "Poetry picks"],
    "cooking": ["Quick healthy recipes", "Baking 101 series", "Vegetarian meal plan"],
    "travel": ["Weekend getaway ideas", "Budget travel tips", "Cultural guides"]
}


def run_demo():
    print("Génération des données synthétiques...")
    df = generate_users(200)

    print("Prétraitement rapide: suppression des doublons (s'il y en a)...")
    df = df.drop_duplicates(subset=["name"]).reset_index(drop=True)

    # analyse exploratoire
    print("Création des visualisations...")
    plot_interest_distribution(df)
    mat = activity_matrix(df)
    plot_activity_heatmap(mat)

    # tests statistiques simples
    from scipy import stats
    # distribution des intérêts observée
    all_interests = [i for row in df["interests"] for i in row]
    counts = [all_interests.count(k) for k in CONTENT_CATALOG.keys()]
    expected = [sum(counts)/len(counts)] * len(counts)
    chi2, p = stats.chisquare(counts, f_exp=expected)
    print(f"Chi2: {chi2:.2f}, p-value: {p:.4f}")

    # recommender
    rec = ContentRecommender(CONTENT_CATALOG)
    sample_user = df.iloc[0].to_dict()
    print("Exemple d'utilisateur:", sample_user["name"], sample_user["interests"])
    suggestions = rec.recommend(sample_user, n=5)
    print("Suggestions pour l'utilisateur:")
    for s in suggestions:
        print("-", s)

    # démonstration de similarité
    other_profiles = [r.to_dict() for _, r in df.sample(10).iterrows()]
    similar_recs = rec.recommend_by_similarity(sample_user, other_profiles, n=3)
    print("Suggestions basées sur utilisateurs similaires:")
    for s in similar_recs:
        print("-", s)

    print("Terminé. Les graphiques ont été sauvegardés dans le dossier courant.")


if __name__ == '__main__':
    run_demo()
