import numpy as np
from scipy import stats


def model_interest_distribution(df, interests):
    """
    Modélisation probabiliste des préférences avec scipy.stats.
    
    Simule une distribution de probabilité pour chaque intérêt basée
    sur la fréquence observée dans les données.
    
    Retourne une dict avec les paramètres de distribution pour chaque intérêt.
    """
    distributions = {}
    
    for interest in interests:
        # Compter les utilisateurs ayant cet intérêt
        count = sum(1 for interests_list in df['interests'] if interest in interests_list)
        prob = count / len(df)
        
        # Modéliser avec une distribution binomiale
        # n = 1 (un utilisateur a ou n'a pas cet intérêt)
        # p = prob (probabilité observée)
        distributions[interest] = {
            'probability': prob,
            'distribution_type': 'binomial',
            'count': count,
            'total_users': len(df)
        }
    
    return distributions


def simulate_preference_distribution(interest_dist, n_simulations=1000):
    """
    Simule des données de préférences basées sur la distribution modélisée.
    
    Utilise scipy.stats pour générer des données synthétiques
    qui suivent les distributions observées.
    """
    simulated_data = {}
    
    for interest, params in interest_dist.items():
        prob = params['probability']
        # Simulation binomiale: chaque utilisateur a une probabilité p d'avoir cet intérêt
        simulated = np.random.binomial(n=1, p=prob, size=n_simulations)
        count = np.sum(simulated)
        simulated_data[interest] = {
            'simulated_count': int(count),
            'simulated_probability': count / n_simulations,
            'observed_probability': prob
        }
    
    return simulated_data


def analyze_distribution_fit(df, interests):
    """
    Analyse la qualité de l'ajustement des distributions observées.
    
    Utilise les fonctions de distribution de scipy.stats pour évaluer
    l'adéquation des données.
    """
    interest_counts = [sum(1 for int_list in df['interests'] if interest in int_list) 
                       for interest in interests]
    
    # Ajustement avec une distribution normale
    mu = np.mean(interest_counts)
    sigma = np.std(interest_counts)
    
    # Test de normalité (Shapiro-Wilk si possible)
    if len(interest_counts) >= 3:
        # Test Kolmogorov-Smirnov contre une distribution normale
        ks_stat, ks_pval = stats.kstest(interest_counts, 'norm', args=(mu, sigma))
    else:
        ks_stat, ks_pval = None, None
    
    return {
        'mean': mu,
        'std': sigma,
        'ks_statistic': ks_stat,
        'ks_pvalue': ks_pval,
        'counts': interest_counts
    }
