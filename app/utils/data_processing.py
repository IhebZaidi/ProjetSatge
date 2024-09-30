import pandas as pd


def create_features(df: pd.DataFrame, label: str = None):
    """
    Crée des caractéristiques à partir du DataFrame des ventes.

    Paramètres :
    - df : DataFrame contenant les données de ventes, avec une colonne 'Date' et 'sales'.
    - label : Nom de la colonne à utiliser comme cible (étiquette) pour la régression.

    Retourne :
    - X : DataFrame des caractéristiques.
    - y : Série des étiquettes si 'label' est fourni.
    """
    # Ajouter des caractéristiques basées sur la date
    df['month'] = df['Date'].dt.month
    df['dayofweek'] = df['Date'].dt.dayofweek
    df['dayofyear'] = df['Date'].dt.dayofyear

    # Ajouter des caractéristiques basées sur les ventes précédentes
    df['lag1'] = df['sales'].shift(1)
    df['lag2'] = df['sales'].shift(2)
    df['lag3'] = df['sales'].shift(3)

    # Ajouter une moyenne mobile des ventes
    df['rolling_mean'] = df['sales'].rolling(window=3).mean()

    # Supprimer les lignes avec des valeurs manquantes
    df = df.dropna()

    # Créer les caractéristiques (X)
    X = df[['month', 'dayofweek', 'dayofyear', 'lag1', 'lag2', 'lag3', 'rolling_mean']]

    if label:
        # Créer les étiquettes (y) si un label est spécifié
        y = df[label]
        return X, y

    return X
