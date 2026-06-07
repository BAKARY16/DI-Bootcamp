"""
visualizer.py
-------------
Génère les graphiques d'analyse avec Matplotlib et Seaborn.
Sauvegarde les images dans le dossier outputs/.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

INTERESTS  = ["technologie", "fitness", "musique", "science", "voyage", "cuisine"]
OUTPUT_DIR = "outputs"
COLORS     = ["#7F77DD", "#1D9E75", "#EF9F27", "#D85A30", "#888780", "#D4537E"]


def setup():
    """Configuration globale des graphiques."""
    sns.set_theme(style="whitegrid", font_scale=1.1)
    plt.rcParams["figure.facecolor"] = "white"
    os.makedirs(OUTPUT_DIR, exist_ok=True)


def plot_interest_distribution(df: pd.DataFrame) -> str:
    """
    Graphique à barres de la répartition des intérêts utilisateurs.
    Sauvegarde : outputs/interest_distribution.png
    """
    # Calcul des fréquences
    counts = {i: 0 for i in INTERESTS}
    for interests_list in df["interests"]:
        lst = interests_list if isinstance(interests_list, list) else eval(interests_list)
        for interest in lst:
            if interest in counts:
                counts[interest] += 1
    
    interests = list(counts.keys())
    values    = [v / len(df) * 100 for v in counts.values()]
    
    # Tri par valeur décroissante
    sorted_pairs = sorted(zip(interests, values, COLORS), key=lambda x: -x[1])
    interests, values, colors = zip(*sorted_pairs)
    
    fig, ax = plt.subplots(figsize=(9, 5))
    bars = ax.barh(interests, values, color=colors, edgecolor="white", height=0.6)
    
    # Valeurs sur les barres
    for bar, val in zip(bars, values):
        ax.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height() / 2,
                f"{val:.1f}%", va="center", fontsize=11, color="#444")
    
    ax.set_xlabel("Pourcentage d'utilisateurs (%)")
    ax.set_title("Répartition des centres d'intérêt", fontsize=14, fontweight="bold", pad=15)
    ax.set_xlim(0, max(values) + 10)
    sns.despine(left=True, bottom=True)
    
    path = os.path.join(OUTPUT_DIR, "interest_distribution.png")
    plt.tight_layout()
    plt.savefig(path, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"[OK] Graphique sauvegardé : {path}")
    return path


def plot_activity_heatmap(df: pd.DataFrame) -> str:
    """
    Heatmap de l'intensité d'activité simulée par heure et catégorie.
    Sauvegarde : outputs/activity_heatmap.png
    """
    # Simulation d'une matrice heure x intérêt (données synthétiques)
    np.random.seed(10)
    hours = [f"{h}h" for h in range(6, 24, 2)]  # 6h à 22h
    
    # Chaque intérêt a un créneau horaire préféré simulé
    peaks = {"technologie": 3, "fitness": 0, "musique": 5,
             "science": 2, "voyage": 4, "cuisine": 6}
    
    matrix = []
    for interest in INTERESTS:
        peak = peaks[interest]
        row  = np.exp(-0.5 * ((np.arange(len(hours)) - peak) ** 2) / 2)
        row  = row + np.random.uniform(0, 0.15, len(hours))
        matrix.append(row)
    
    df_heat = pd.DataFrame(matrix, index=INTERESTS, columns=hours)
    
    fig, ax = plt.subplots(figsize=(11, 5))
    sns.heatmap(df_heat, ax=ax, cmap="YlOrRd", linewidths=0.4,
                annot=True, fmt=".2f", cbar_kws={"label": "Intensité"})
    
    ax.set_title("Intensité d'activité par heure et catégorie", fontsize=14, fontweight="bold", pad=15)
    ax.set_xlabel("Heure de la journée")
    ax.set_ylabel("")
    
    path = os.path.join(OUTPUT_DIR, "activity_heatmap.png")
    plt.tight_layout()
    plt.savefig(path, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"[OK] Graphique sauvegardé : {path}")
    return path


def plot_recommendations_by_segment(df: pd.DataFrame) -> str:
    """
    Graphique à barres groupées : catégories recommandées par tranche d'âge.
    Sauvegarde : outputs/recommendations_chart.png
    """
    # Simulation du nombre de recommandations par segment et catégorie
    np.random.seed(7)
    segments = ["18-25", "26-35", "36-50", "51-65"]
    
    # Nombre de recommandations simulées par segment et intérêt
    recs_data = {
        "technologie": [85, 72, 55, 30],
        "musique":     [78, 65, 48, 40],
        "fitness":     [60, 80, 70, 55],
        "science":     [40, 55, 62, 70],
        "voyage":      [50, 60, 68, 50],
        "cuisine":     [30, 45, 58, 75],
    }
    
    x     = np.arange(len(segments))
    width = 0.13
    
    fig, ax = plt.subplots(figsize=(12, 6))
    
    for i, (interest, values) in enumerate(recs_data.items()):
        offset = (i - len(recs_data) / 2) * width + width / 2
        ax.bar(x + offset, values, width, label=interest,
               color=COLORS[i], edgecolor="white")
    
    ax.set_xlabel("Tranche d'âge")
    ax.set_ylabel("Nombre de recommandations")
    ax.set_title("Catégories recommandées par segment d'utilisateurs",
                 fontsize=14, fontweight="bold", pad=15)
    ax.set_xticks(x)
    ax.set_xticklabels(segments)
    ax.legend(title="Catégorie", bbox_to_anchor=(1.01, 1), loc="upper left")
    sns.despine()
    
    path = os.path.join(OUTPUT_DIR, "recommendations_chart.png")
    plt.tight_layout()
    plt.savefig(path, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"[OK] Graphique sauvegardé : {path}")
    return path


def generate_all(df: pd.DataFrame) -> list:
    """Lance la génération de tous les graphiques."""
    setup()
    print("\n=== Génération des visualisations ===")
    paths = [
        plot_interest_distribution(df),
        plot_activity_heatmap(df),
        plot_recommendations_by_segment(df),
    ]
    print(f"\n[OK] {len(paths)} graphiques générés dans /{OUTPUT_DIR}/")
    return paths


if __name__ == "__main__":
    from data_processor import process
    df = process()
    generate_all(df)
