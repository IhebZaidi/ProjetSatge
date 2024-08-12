from lightgbm import LGBMRegressor

class LightGBMModel:
    def __init__(self):
        self.model = LGBMRegressor()

    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)
        return self.model

    def predict(self, X_test):
        return self.model.predict(X_test)
