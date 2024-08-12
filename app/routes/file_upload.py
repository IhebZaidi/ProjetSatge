# app/routes/file_upload.py
from fastapi import APIRouter, File, UploadFile, HTTPException
import pandas as pd
from app.state import state

router = APIRouter()

@router.post("/upload_csv/")
async def upload_csv(file: UploadFile = File(...)):
    if file.content_type != 'text/csv':
        raise HTTPException(status_code=400, detail="Invalid file type. Please upload a CSV file.")

    state.uploaded_df = pd.read_csv(file.file)
    state.uploaded_df['Date'] = pd.to_datetime(state.uploaded_df['date'])
    state.uploaded_df = state.uploaded_df.dropna().sort_values('Date')

    # Journaliser le DataFrame téléchargé pour débogage
    print(f"DataFrame uploaded: {state.uploaded_df.head()}")

    return {"message": "File processed successfully"}
