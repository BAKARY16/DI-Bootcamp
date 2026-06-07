import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def plot_interest_distribution(df, out_path="interest_distribution.png"):
    # flatten interests
    all_interests = [i for row in df["interests"] for i in row]
    counts = pd.Series(all_interests).value_counts()
    plt.figure(figsize=(8, 5))
    sns.barplot(data=pd.DataFrame({'interest': counts.index, 'count': counts.values}), 
                x='interest', y='count', palette="viridis", hue='interest', legend=False)
    plt.title("Répartition des centres d'intérêt")
    plt.xlabel("Centre d'intérêt")
    plt.ylabel("Nombre d'utilisateurs")
    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()


def plot_activity_heatmap(mat, out_path="activity_heatmap.png"):
    plt.figure(figsize=(10, 6))
    sns.heatmap(mat.T, cmap="magma", annot=False)
    plt.title("Intensité d'activité par heure et par catégorie")
    plt.xlabel("Heure")
    plt.ylabel("Catégorie")
    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()


def plot_recommendations_by_segment(segment_recs, out_path="recommendations_by_segment.png"):
    """
    Graphique des recommandations par segment d'utilisateurs.
    
    Affiche les catégories les plus recommandées par groupe d'âge.
    """
    # Construire un DataFrame pour la visualisation
    segments_list = []
    for segment, category_counts in segment_recs.items():
        for category, count in category_counts.items():
            segments_list.append({'Segment': segment, 'Catégorie': category, 'Nombre': count})
    
    if not segments_list:
        print("Pas de données pour le graphique des recommandations par segment")
        return
    
    df_seg = pd.DataFrame(segments_list)
    
    plt.figure(figsize=(10, 6))
    sns.barplot(data=df_seg, x='Segment', y='Nombre', hue='Catégorie', palette='husl')
    plt.title("Recommandations par segment d'utilisateurs")
    plt.xlabel("Segment d'âge")
    plt.ylabel("Nombre de recommandations")
    plt.legend(title='Catégorie', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()
