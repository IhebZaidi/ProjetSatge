def create_features(df, label=None):
    df['month'] = df['Date'].dt.month
    df['dayofweek'] = df['Date'].dt.dayofweek
    df['dayofyear'] = df['Date'].dt.dayofyear
    df['lag1'] = df['sales'].shift(1)
    df['lag2'] = df['sales'].shift(2)
    df['lag3'] = df['sales'].shift(3)
    df['rolling_mean'] = df['sales'].rolling(window=3).mean()
    df = df.dropna()
    X = df[['month', 'dayofweek', 'dayofyear', 'lag1', 'lag2', 'lag3', 'rolling_mean']]
    if label:
        y = df[label]
        return X, y
    return X
