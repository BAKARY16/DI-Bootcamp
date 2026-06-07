"""
data_processor.py
-----------------
Nettoie et prétraite les données brutes des utilisateurs.
Supprime les doublons, gère les valeurs manquantes, normalise les colonnes.
"""

import pandas as pd
import json
import os


def load_raw_data(path: str = "data/raw/users_raw.csv") -> pd.DataFrame:
    """Charge les données brutes depuis le CSV."""
    df = pd.read_csv(path)
    print(f"[OK] Données chargées : {len(df)} lignes, {len(df.columns)} colonnes")
    return df


def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """Supprime les lignes dupliquées."""
    before = len(df)
    df = df.drop_duplicates(subset=["user_id"])
    after = len(df)
    print(f"[OK] Doublons supprimés : {before - after} lignes retirées")
    return df


def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """Remplace les valeurs manquantes par des valeurs par défaut."""
    # Âge manquant → médiane
    if df["age"].isnull().any():
        median_age = int(df["age"].median())
        df["age"] = df["age"].fillna(median_age)
        print(f"[OK] Âges manquants remplis avec la médiane : {median_age}")
    
    # Intérêts manquants → liste vide
    df["interests"] = df["interests"].fillna('[]')
    df["activity_log"] = df["activity_log"].fillna('[]')
    
    print(f"[OK] Valeurs manquantes traitées. Restantes : {df.isnull().sum().sum()}")
    return df


def parse_json_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Convertit les colonnes JSON (string) en vraies listes Python."""
    df["interests"] = df["interests"].apply(json.loads)
    df["activity_log"] = df["activity_log"].apply(json.loads)
    return df


def add_features(df: pd.DataFrame) -> pd.DataFrame:
    """Ajoute des colonnes calculées utiles pour l'analyse."""
    df["age_group"] = pd.cut(
        df["age"],
        bins=[17, 25, 35, 50, 65],
        labels=["18-25", "26-35", "36-50", "51-65"]
    )
    # Nombre d'intérêts si pas déjà calculé
    if "n_interests" not in df.columns:
        df["n_interests"] = df["interests"].apply(len)
    if "n_activities" not in df.columns:
        df["n_activities"] = df["activity_log"].apply(len)
    
    print("[OK] Nouvelles colonnes ajoutées : age_group, n_interests, n_activities")
    return df


def save_clean_data(df: pd.DataFrame, path: str = "data/processed/users_clean.csv") -> None:
    """Sauvegarde les données nettoyées (listes reconverties en JSON string)."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df_save = df.copy()
    df_save["interests"] = df_save["interests"].apply(json.dumps)
    df_save["activity_log"] = df_save["activity_log"].apply(json.dumps)
    df_save.to_csv(path, index=False)
    print(f"[OK] Données nettoyées sauvegardées : {path}")


def process(raw_path: str = "data/raw/users_raw.csv",
            clean_path: str = "data/processed/users_clean.csv") -> pd.DataFrame:
    """Pipeline complet de traitement."""
    print("\n--- Traitement des données ---")
    df = load_raw_data(raw_path)
    df = remove_duplicates(df)
    df = handle_missing_values(df)
    df = parse_json_columns(df)
    df = add_features(df)
    save_clean_data(df, clean_path)
    return df


if __name__ == "__main__":
    df = process()
    print(f"\nAperçu :\n{df[['user_id', 'name', 'age', 'age_group', 'n_interests']].head(5)}")
