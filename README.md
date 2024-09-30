
# Projet FastAPI de Prévision des Séries Temporelles

## Structure du Projet

```
projet-stage /
│
├── app/
│   ├── main.py
│   ├── dependencies.py
│   ├── file_manager.py
│   ├── models/
│   │   ├── random_forest.py
│   │   ├── lightgbm.py
│   │   ├── xgboost.py
│   │   ├── lstm.py
│   ├── utils/
│   │   ├── data_processing.py
│   │   ├── evaluation.py
│   ├── routes/
│   │   ├── file_upload.py
│   │   ├── train.py
│   │   ├── static_files.py 
│   ├── state.py 
├── plots/
│   └── (fichiers de graphiques générés)
├── frontend/
│   ├── img.png
│   ├── index.html
│   ├── style.css
│   ├── script.js
├── Dockerfile  
└── requirements.txt 
```

## Installation

1. **Cloner le dépôt :**

   ```bash
   git https://github.com/IhebZaidi/ProjetSatge.git
   cd projet-stage 
   ```

2. **Créer un environnement virtuel :**

   ```bash
   python -m venv env
   source env/bin/activate  # Sur Windows, utilisez `env\Scriptsctivate`
   ```

3. **Installer les dépendances :**

   ```bash
   pip install -r requirements.txt
   ```

## Utilisation

### Lancer l'application

Pour démarrer le serveur FastAPI, exécutez :

```bash
uvicorn app.main:app --reload
```

L'application sera disponible sur `http://127.0.0.1:8000`.

### API Endpoints

1. **Télécharger un fichier CSV :**

   ```
   POST /upload_csv/
   ```

   Ce point de terminaison permet de télécharger un fichier CSV pour l'analyse des séries temporelles. Le fichier doit contenir une colonne `date` et une colonne `sales`.

2. **Entraîner un modèle :**

   ```
   POST /train_model/
   ```

   Ce point de terminaison entraîne un modèle de prévision sur les données téléchargées. Vous pouvez choisir parmi les modèles suivants : `RandomForest`, `LightGBM`, `XGBoost`, `LSTM`.

3. **Récupérer un fichier statique :**

   ```
   GET /static/{file_name}
   ```

   Ce point de terminaison permet de récupérer un fichier statique, tel qu'un graphique généré lors de l'entraînement du modèle.

## Docker

Pour containeriser l'application, vous pouvez utiliser le `Dockerfile` inclus. Suivez les étapes suivantes :

1. **Construire l'image Docker :**

   ```bash
   docker build -t projet-stage .
   ```

2. **Exécuter le conteneur :**

   ```bash
   docker run -p 8000:8000 projet-stage 
   ```

L'application sera disponible sur `http://127.0.0.1:8000`.

## Contribuer

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou à soumettre une pull request.
