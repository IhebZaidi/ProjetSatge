from sklearn.metrics import (
    mean_squared_error,
    r2_score,
    mean_absolute_error,
    mean_absolute_percentage_error,
    explained_variance_score
)
import numpy as np


def evaluate_model(y_true, y_pred):
    """
    Évalue les performances du modèle en utilisant diverses métriques de régression.

    Paramètres :
    - y_true : Valeurs réelles (observées).
    - y_pred : Valeurs prédites par le modèle.

    Retourne :
    - mse : Erreur quadratique moyenne (Mean Squared Error).
    - rmse : Racine de l'erreur quadratique moyenne (Root Mean Squared Error).
    - r2 : Coefficient de détermination (R²).
    - mae : Erreur absolue moyenne (Mean Absolute Error).
    - mape : Erreur absolue moyenne en pourcentage (Mean Absolute Percentage Error).
    - evs : Variance expliquée (Explained Variance Score).
    """
    # Calculer les métriques d'évaluation
    mse = mean_squared_error(y_true, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_true, y_pred)
    mae = mean_absolute_error(y_true, y_pred)
    mape = mean_absolute_percentage_error(y_true, y_pred) * 100
    evs = explained_variance_score(y_true, y_pred)

    return mse, rmse, r2, mae, mape, evs
