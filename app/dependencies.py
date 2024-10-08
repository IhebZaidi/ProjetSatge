from fastapi import Query, HTTPException
from app.models.random_forest import RandomForestModel
from app.models.lightgbm import LightGBMModel
from app.models.xgboost import XGBoostModel
from app.models.lstm import LSTMModel

AVAILABLE_MODELS = ['RandomForest', 'LightGBM', 'XGBoost', 'LSTM']

def get_model(model_name: str = Query(..., enum=AVAILABLE_MODELS)):
    if model_name == 'RandomForest':
        return RandomForestModel.get_instance()
    elif model_name == 'LightGBM':
        return LightGBMModel.get_instance()
    elif model_name == 'XGBoost':
        return XGBoostModel.get_instance()
    elif model_name == 'LSTM':
        return LSTMModel.get_instance()
    else:
        raise HTTPException(status_code=400, detail="Invalid model name.")
