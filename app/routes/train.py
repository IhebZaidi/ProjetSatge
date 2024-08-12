# app/routes/train.py
from fastapi import APIRouter, Query, HTTPException
import numpy as np
import matplotlib.pyplot as plt
from app.utils.data_processing import create_features
from app.utils.evaluation import evaluate_model
from pathlib import Path
import wandb
from app.state import state
from sklearn.model_selection import train_test_split

from fastapi import FastAPI, File, UploadFile, HTTPException, Query
from fastapi.responses import StreamingResponse
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
from pathlib import Path
from sklearn.ensemble import RandomForestRegressor
from lightgbm import LGBMRegressor
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error, mean_absolute_percentage_error, \
    explained_variance_score
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.optimizers import Adam
import wandb
router = APIRouter()

plot_dir = Path("plots")
plot_dir.mkdir(exist_ok=True)

AVAILABLE_MODELS = ['RandomForest', 'LightGBM', 'XGBoost', 'LSTM']

@router.post("/train_model/")
async def train_model(model_name: str = Query(..., enum=AVAILABLE_MODELS, description="Choose model from available options")):
    if state.uploaded_df is None:
        raise HTTPException(status_code=400, detail="No CSV file has been uploaded yet. Please upload a CSV file first.")

    if model_name not in AVAILABLE_MODELS:
        raise HTTPException(status_code=400, detail="Invalid model name. Choose from the available models.")

    # Journaliser le DataFrame pour débogage
    print(f"DataFrame for training: {state.uploaded_df.head()}")

    # Créer les caractéristiques et diviser les données
    X, y = create_features(state.uploaded_df, label='sales')
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

    # Entraîner le modèle et prédire sur les données de test
    if model_name == 'LSTM':
        # Reshape pour LSTM
        X_train_lstm = np.array(X_train).reshape((X_train.shape[0], X_train.shape[1], 1))
        X_test_lstm = np.array(X_test).reshape((X_test.shape[0], X_test.shape[1], 1))

        model = Sequential()
        model.add(LSTM(50, activation='relu', input_shape=(X_train_lstm.shape[1], 1)))
        model.add(Dense(1))
        model.compile(optimizer=Adam(learning_rate=0.001), loss='mse')

        model.fit(X_train_lstm, y_train, epochs=20, batch_size=32, verbose=1, validation_split=0.2)
        y_pred = model.predict(X_test_lstm).flatten()
    else:
        if model_name == 'RandomForest':
            model = RandomForestRegressor()
        elif model_name == 'LightGBM':
            model = LGBMRegressor()
        elif model_name == 'XGBoost':
            model = XGBRegressor()

        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

    # Évaluer le modèle uniquement sur les données de test
    mse, rmse, r2, mae, mape, evs = evaluate_model(y_test, y_pred)

    # Journaliser les métriques sur W&B
    wandb.log({
        f'{model_name}_MSE': mse,
        f'{model_name}_RMSE': rmse,
        f'{model_name}_R2': r2,
        f'{model_name}_MAE': mae,
        f'{model_name}_MAPE': mape,
        f'{model_name}_EVS': evs
    })

    # Générer le graphique et le sauvegarder dans un fichier
    split_index = len(X_train)
    train_dates = state.uploaded_df['Date'].iloc[:split_index]
    test_dates = state.uploaded_df['Date'].iloc[split_index:split_index + len(y_test)]

    plot_file = plot_dir / f"{model_name}_plot.png"
    plt.figure(figsize=(14, 7))

    plt.plot(state.uploaded_df['Date'].iloc[:split_index], state.uploaded_df['sales'].iloc[:split_index], label='Training Sales', color='blue')
    plt.plot(state.uploaded_df['Date'].iloc[split_index:split_index + len(y_test)], state.uploaded_df['sales'].iloc[split_index:split_index + len(y_test)], label='Test Sales', color='green')
    plt.plot(test_dates, y_pred, label=f'{model_name} Predictions', color='orange')

    plt.legend()
    plt.title(f'{model_name} Predictions on Training and Test Data')
    plt.xlabel('Date')
    plt.ylabel('Sales')
    plt.grid(True)
    plt.savefig(plot_file)
    plt.close()

    plot_url = f"http://localhost:8000/static/{plot_file.name}"

    return {"message": f"{model_name} model trained successfully", "metrics": {"MSE": mse, "RMSE": rmse, "R2": r2, "MAE": mae, "MAPE": mape, "EVS": evs}, "plot_url": plot_url}
