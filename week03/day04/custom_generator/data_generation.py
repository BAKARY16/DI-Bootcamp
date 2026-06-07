import random
from datetime import datetime
import numpy as np
import pandas as pd

INTERESTS = ["fitness", "technology", "music", "books", "cooking", "travel"]

ACTIVITY_TEMPLATES = [
    "watched {topic} at {hour}",
    "listened to {topic} at {hour}",
    "bought {topic} at {hour}",
    "viewed {topic} at {hour}"
]


def generate_users(n=200, seed=0):
    random.seed(seed)
    np.random.seed(seed)

    # make interests distribution: fitness more common
    weights = np.array([0.25, 0.15, 0.2, 0.15, 0.15, 0.1])
    weights = weights / weights.sum()

    rows = []
    for i in range(n):
        name = f"User_{i+1}"
        age = int(np.random.normal(30, 10))
        if age < 16:
            age = 16
        # each user has 1-3 interests
        k = np.random.randint(1, 4)
        interests = list(np.random.choice(INTERESTS, size=k, replace=False, p=weights))

        # activity log: generate 1-8 events with random hour and topic (use interests sometimes)
        m = np.random.randint(1, 9)
        activity_log = []
        for _ in range(m):
            hour = np.random.randint(0, 24)
            # pick topic with higher probability from user's interests
            if random.random() < 0.7:
                topic = random.choice(interests)
            else:
                topic = random.choice(INTERESTS)
            template = random.choice(ACTIVITY_TEMPLATES)
            activity_log.append(template.format(topic=topic, hour=hour))

        rows.append({
            "name": name,
            "age": age,
            "interests": interests,
            "activity_log": activity_log
        })

    df = pd.DataFrame(rows)
    return df


def activity_matrix(df):
    # returns a pivot table (hours x interest) counting events
    hours = range(24)
    mat = pd.DataFrame(0, index=hours, columns=INTERESTS)
    for _, row in df.iterrows():
        for ev in row["activity_log"]:
            # parse hour and topic
            try:
                parts = ev.rsplit("at", 1)
                topic = parts[0].split()[-1]
                hour = int(parts[1])
                if topic in mat.columns and 0 <= hour < 24:
                    mat.loc[hour, topic] += 1
            except Exception:
                continue
    return mat
