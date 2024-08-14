from fastapi import FastAPI
from app.routes import file_upload, train, static_files  # Import des modules de routes
import wandb

# Initialisation de WandB pour le suivi des expériences
wandb.init(project="STAGE", name="testA")

app = FastAPI()

# Enregistrement des routeurs pour les différentes fonctionnalités
app.include_router(file_upload.router)  # Route pour le téléchargement de fichiers
app.include_router(train.router)  # Route pour l'entraînement des modèles
app.include_router(static_files.router)  # Route pour les fichiers statiques

if __name__ == '__main__':
    import uvicorn
    # Démarrage de l'application FastAPI avec Uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
