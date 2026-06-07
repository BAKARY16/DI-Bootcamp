import numpy as np
from scipy import stats


class User:
    """Représente un utilisateur avec ses attributs."""
    
    def __init__(self, name, age, interests, activity_log):
        self.name = name
        self.age = age
        self.interests = interests
        self.activity_log = activity_log
    
    def __repr__(self):
        return f"User({self.name}, {self.age}, {self.interests})"


class Content:
    """Représente un contenu recommandable."""
    
    def __init__(self, title, category, target_age_min=10, target_age_max=100):
        self.title = title
        self.category = category
        self.target_age_min = target_age_min
        self.target_age_max = target_age_max
    
    def is_suitable_for_user(self, user):
        """Vérifie si le contenu convient à l'utilisateur."""
        return self.target_age_min <= user.age <= self.target_age_max
    
    def __repr__(self):
        return f"Content({self.title}, {self.category})"


class RecommendationEngine:
    """Moteur de recommandation basé sur les intérêts et l'activité."""
    
    def __init__(self, content_catalog):
        """
        Args:
            content_catalog: Dict[category] -> List[Content]
        """
        self._catalog = content_catalog
    
    def recommend(self, user, n=5):
        """
        Génère des recommandations personnalisées basées sur les intérêts.
        
        Adaptation dynamique: Le score augmente si l'intérêt est mentionné
        dans l'historique d'activité.
        """
        scores = {}
        for category, contents in self._catalog.items():
            score = 0
            # Intérêt explicite
            if category in user.interests:
                score += 2
            # Mentions dans l'activité (adaptation dynamique)
            mentions = sum(1 for activity in user.activity_log if category in activity)
            score += mentions * 0.5
            # Filtre par âge
            suitable_contents = [c for c in contents if c.is_suitable_for_user(user)]
            scores[category] = (score, suitable_contents)
        
        # Trier par score
        ranked = sorted(scores.items(), key=lambda x: x[0], reverse=True)
        
        # Construire les recommandations
        recommendations = []
        for category, (score, contents) in ranked:
            recommendations.extend(contents[:n // len(scores) + 1])
        
        return recommendations[:n]
    
    def recommend_by_segment(self, users, segment_key='age'):
        """
        Recommandations par segment d'utilisateurs.
        
        Utile pour analyser les patterns par groupe d'âge ou autre.
        """
        segments = {}
        for user in users:
            if segment_key == 'age':
                age_group = (user.age // 10) * 10
                key = f"{age_group}-{age_group + 9}"
            else:
                key = segment_key
            
            if key not in segments:
                segments[key] = []
            segments[key].append(user)
        
        # Recommandations par segment
        segment_recs = {}
        for segment, segment_users in segments.items():
            category_counts = {}
            for user in segment_users:
                for category in user.interests:
                    category_counts[category] = category_counts.get(category, 0) + 1
            segment_recs[segment] = category_counts
        
        return segment_recs
