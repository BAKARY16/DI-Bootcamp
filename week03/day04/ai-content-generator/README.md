# AI Content Generator

Système de recommandation de contenu personnalisé basé sur l'IA.

## Structure du projet

```
ai-content-generator/
├── backend/          # Cœur Python (NumPy, Pandas, SciPy, Matplotlib)
│   ├── src/          # Modules Python
│   ├── data/         # Données brutes, nettoyées, exports
│   ├── outputs/      # Graphiques générés
│   └── main.py       # Point d'entrée
└── frontend/         # Interface React JS
    └── src/          # Composants React
```

## Lancement rapide

### Backend
```bash
cd backend
pip install -r requirements.txt
python main.py
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

## Modules backend

| Fichier | Rôle |
|---|---|
| `data_generator.py` | Génère 500 profils synthétiques |
| `data_processor.py` | Nettoyage et prétraitement |
| `analyzer.py` | Analyse statistique SciPy |
| `recommender.py` | Moteur de recommandation OOP |
| `visualizer.py` | Graphiques Matplotlib / Seaborn |
| `api.py` | API Flask pour le frontend |
