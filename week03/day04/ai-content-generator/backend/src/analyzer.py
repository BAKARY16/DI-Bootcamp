"""
analyzer.py
-----------
Analyse statistique des profils utilisateurs.
Utilise SciPy pour les distributions de probabilité et le test du chi-carré (χ²).
"""

import pandas as pd
import numpy as np
from scipy import stats


INTERESTS = ["technologie", "fitness", "musique", "science", "voyage", "cuisine"]


def compute_interest_distribution(df: pd.DataFrame) -> dict:
    """
    Calcule la fréquence de chaque intérêt dans la population.
    Retourne un dictionnaire {intérêt: fréquence (0 à 1)}.
    """
    counts = {interest: 0 for interest in INTERESTS}
    
    for interests_list in df["interests"]:
        for interest in interests_list:
            if interest in counts:
                counts[interest] += 1
    
    total = len(df)
    frequencies = {k: round(v / total, 4) for k, v in counts.items()}
    
    print("\n--- Distribution des intérêts ---")
    for interest, freq in sorted(frequencies.items(), key=lambda x: -x[1]):
        bar = "█" * int(freq * 30)
        print(f"  {interest:<15} {bar} {freq:.1%}")
    
    return frequencies


def chi_square_test(df: pd.DataFrame) -> list:
    """
    Applique le test χ² pour analyser si certaines activités sont
    statistiquement liées à certains intérêts.
    
    Retourne une liste de résultats avec p-value et conclusion.
    """
    print("\n--- Test du Chi-carré (χ²) ---")
    
    results = []
    
    # Test 1 : "watched AI talk" corrélé à l'intérêt "technologie" ?
    has_ai_talk   = df["activity_log"].apply(lambda a: "watched AI talk" in a)
    has_tech      = df["interests"].apply(lambda i: "technologie" in i)
    
    # Tableau de contingence
    table1 = pd.crosstab(has_ai_talk, has_tech)
    chi2, p, dof, _ = stats.chi2_contingency(table1)
    result1 = {
        "paire": "AI talk → technologie",
        "chi2": round(chi2, 2),
        "p_value": round(p, 4),
        "significatif": p < 0.05
    }
    results.append(result1)
    print(f"  {result1['paire']:<30} χ²={result1['chi2']:<8} p={result1['p_value']:<8} {'✓ Significatif' if result1['significatif'] else '— Non significatif'}")
    
    # Test 2 : écoute de musique rock → intérêt "musique" ?
    has_rock  = df["activity_log"].apply(lambda a: "listened to rock music" in a)
    has_music = df["interests"].apply(lambda i: "musique" in i)
    
    table2 = pd.crosstab(has_rock, has_music)
    chi2, p, dof, _ = stats.chi2_contingency(table2)
    result2 = {
        "paire": "Rock music → musique",
        "chi2": round(chi2, 2),
        "p_value": round(p, 4),
        "significatif": p < 0.05
    }
    results.append(result2)
    print(f"  {result2['paire']:<30} χ²={result2['chi2']:<8} p={result2['p_value']:<8} {'✓ Significatif' if result2['significatif'] else '— Non significatif'}")
    
    # Test 3 : workout → intérêt "fitness" ?
    has_workout = df["activity_log"].apply(lambda a: "completed workout" in a)
    has_fitness = df["interests"].apply(lambda i: "fitness" in i)
    
    table3 = pd.crosstab(has_workout, has_fitness)
    chi2, p, dof, _ = stats.chi2_contingency(table3)
    result3 = {
        "paire": "Workout → fitness",
        "chi2": round(chi2, 2),
        "p_value": round(p, 4),
        "significatif": p < 0.05
    }
    results.append(result3)
    print(f"  {result3['paire']:<30} χ²={result3['chi2']:<8} p={result3['p_value']:<8} {'✓ Significatif' if result3['significatif'] else '— Non significatif'}")
    
    return results


def probability_distribution_analysis(frequencies: dict) -> None:
    """
    Simule la distribution de probabilité de chaque intérêt.
    Utilise scipy.stats pour calculer moyenne et écart-type.
    """
    print("\n--- Analyse des distributions de probabilité ---")
    values = list(frequencies.values())
    
    mean = np.mean(values)
    std  = np.std(values)
    
    print(f"  Moyenne globale : {mean:.2%}")
    print(f"  Écart-type      : {std:.4f}")
    
    # Teste si la distribution suit une loi normale
    stat, p = stats.normaltest(values)
    print(f"  Test normalité  : p={p:.4f} → {'Distribution normale' if p > 0.05 else 'Distribution non normale'}")


def analyze(df: pd.DataFrame) -> dict:
    """Lance l'analyse complète et retourne les résultats."""
    print("\n=== Analyse statistique ===")
    frequencies = compute_interest_distribution(df)
    chi2_results = chi_square_test(df)
    probability_distribution_analysis(frequencies)
    return {
        "frequencies": frequencies,
        "chi2_results": chi2_results
    }


if __name__ == "__main__":
    from data_processor import process
    df = process()
    analyze(df)
