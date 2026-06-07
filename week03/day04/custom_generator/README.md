Projet: Générateur de contenu personnalisé (Hackathon)

But: Ce projet vise à créer un générateur de contenu personnalisé pour une plateforme de streaming fictive. L'objectif est de modéliser les préférences des utilisateurs, d'analyser les données de manière statistique et de recommander du contenu pertinent. Le projet doit démontrer la maîtrise de la manipulation de données, de l'analyse statistique, de la programmation orientée objet et de la visualisation.

## Membre de l'équipe
- BAKARY SINON qui a contribué à l'analyse statistique et à la visualisation.
- BENNY TAPE qui a contribué à la génération de données et à l'analyse statistique.

## Structure du projet

**Backend (Python)**
- `data_generation.py` : génération synthétique de profils utilisateurs (Partie 1 & 2)
- `statistical_analysis.py` : modélisation probabiliste des préférences (Partie 3.1)
- `recommender.py` : moteur de recommandation simple (ancien)
- `recommender_v2.py` : classes User, Content, RecommendationEngine avec POO (Partie 4)
- `visualize.py` : graphiques Matplotlib/Seaborn (Partie 5)
- `main.py` : pipeline d'exécution basique
- `dashboard.py` : serveur web + génération données frontend

**Frontend (HTML/CSS/JS)**
- `frontend/index.html` : interface avec onglets
- `frontend/style.css` : styles modernes
- `frontend/app.js` : chargement dynamique et graphiques Chart.js
- `frontend/data.json` : données générées par le backend

**Documentation**
- `demo.ipynb` : notebook complet démontrant tous les critères
- `requirements.txt` : dépendances
- `README.md` : ce fichier

## Conformité au barème (100 points)

###  Partie 1 - Conception et modélisation 
- **Classe User** : structure avec name, age, interests, activity_log
- **Génération** : 100+ profils variés avec intérêts et activités réalistes

###  Partie 2 - Manipulation et préparation 
- **NumPy/Pandas** : génération et manipulation DataFrame
- **Nettoyage** : drop_duplicates, gestion valeurs manquantes
- **EDA** : statistiques descriptives, analyse des intérêts et activités

###  Partie 3 - Analyse statistique 
- **Modélisation probabiliste** : scipy.stats.binomial pour distributions
- **Test Chi²** : scipy.stats.chisquare avec interprétation p-value
- **Simulation** : génération de données synthétiques basée sur distributions

###  Partie 4 - Moteur de recommandation 
- **Classe User** : encapsulation avec attributs privés
- **Classe Content** : représente un contenu avec filtrage d'âge
- **Classe RecommendationEngine** : moteur de recommandation polymorphe
- **Recommandations personnalisées** : logique de scoring basée sur intérêts
- **Adaptation dynamique** : score augmente si intérêt mentionné dans activité
- **Similarité (SciPy)** : calcul avec cosine/euclidean distance

###  Partie 5 - Visualisation 
- **Répartition intérêts** : graphique à barres (Matplotlib/Seaborn)
- **Heatmap activité** : intensité par heure et catégorie
- **Recommandations par segment** : analyse par groupe d'âge

### Bonus - Interface interactive 
- Dashboard web avec onglets
- Graphiques dynamiques avec Chart.js
- Données JSON générées automatiquement
- Interface professionnelle et responsive

## Installation et exécution

1. Créez un environnement virtuel Python 3.8+.
2. Installez les dépendances:

1. Créez un environnement virtuel Python 3.8+.
2. Installez les dépendances:

```
python -m pip install -r requirements.txt
```

3. Lancez la démonstration:

```
python main.py
```

4. Lancez le dashboard:

```
python dashboard.py
```

Puis ouvrez l'URL indiquée, ou utilisez directement `frontend/index.html`.

Notes:
- Le projet respecte l'usage unique des bibliothèques listées.
- Le code montre l'usage de fonctions, lambdas, map/filter/reduce et POO.
- Le dashboard est dynamique : il lit `frontend/data.json` et affiche des graphiques interactifs avec Chart.js.
- L'interface est structurée en onglets pour séparer l'analyse, les données, les graphiques et les recommandations.
