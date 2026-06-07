from functools import reduce
import numpy as np
from scipy.spatial import distance


class Recommender:
    """Base recommender class demonstrating encapsulation and polymorphism."""

    def __init__(self, content_catalog):
        # contenu disponible par catégorie
        self._catalog = content_catalog  # encapsulé (privé)

    def recommend(self, user_profile, n=5):
        raise NotImplementedError()


class ContentRecommender(Recommender):
    """Simple recommender that uses interests and activity to score items."""

    def __init__(self, content_catalog):
        super().__init__(content_catalog)

    def recommend(self, user_profile, n=5):
        # score categories by presence in interests and activity intensity
        interests = user_profile.get("interests", [])
        activity_log = user_profile.get("activity_log", [])

        # basic scoring: interest presence + activity mentions
        scores = {cat: 0 for cat in self._catalog}
        for cat in scores:
            scores[cat] += (1 if cat in interests else 0)
            # count mentions in activity_log
            mentions = sum(1 for ev in activity_log if cat in ev)
            scores[cat] += 0.1 * mentions

        # rank categories
        ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)

        # build recommendations using map and lambda
        recs = list(
            map(lambda c: self._catalog[c[0]][:n], ranked)
        )
        # flatten
        flat = reduce(lambda a, b: a + b, recs, [])
        return flat[:n]

    def recommend_by_similarity(self, user_profile, other_profiles, n=5, metric="cosine"):
        # build vector per profile for interests
        cats = list(self._catalog.keys())

        def profile_vector(p):
            return np.array([1 if c in p.get("interests", []) else 0 for c in cats], dtype=float)

        target = profile_vector(user_profile)
        others = [profile_vector(p) for p in other_profiles]

        # compute distances
        if metric == "cosine":
            dists = [distance.cosine(target, o) for o in others]
        else:
            dists = [distance.euclidean(target, o) for o in others]

        # pick most similar
        idx = int(np.argmin(dists))
        similar = other_profiles[idx]
        # merge suggestions from similar user
        return self.recommend(similar, n=n)
