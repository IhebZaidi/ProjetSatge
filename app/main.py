from fastapi import FastAPI
from app.routes import file_upload, train, static_files  # Importer le nouveau fichier de routes
import wandb

wandb.init(project="STAGE", name="testA")

app = FastAPI()

# Registering routes
app.include_router(file_upload.router)
app.include_router(train.router)
app.include_router(static_files.router)  # Enregistrement de la nouvelle route

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
