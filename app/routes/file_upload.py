from fastapi import APIRouter, File, UploadFile, HTTPException
import pandas as pd
from app.state import State

router = APIRouter()


@router.post("/upload_csv/")
async def upload_csv(file: UploadFile = File(...)):
    if file.content_type != 'text/csv':
        raise HTTPException(status_code=400, detail="Invalid file type. Please upload a CSV file.")

    # Utiliser l'instance singleton de State
    state = State.get_instance()

    # Lire le fichier CSV
    try:
        state.uploaded_df = pd.read_csv(file.file)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error reading CSV file: {e}")

    # Vérifier les colonnes nécessaires
    if 'date' not in state.uploaded_df.columns:
        raise HTTPException(status_code=400, detail="CSV file must contain a 'date' column.")

    # Convertir les dates et nettoyer le DataFrame
    state.uploaded_df['Date'] = pd.to_datetime(state.uploaded_df['date'], errors='coerce')
    state.uploaded_df = state.uploaded_df.dropna().sort_values('Date')

    # Journaliser le DataFrame téléchargé pour débogage
    print(f"DataFrame uploaded: {state.uploaded_df.head()}")

    return {"message": "File processed successfully"}
