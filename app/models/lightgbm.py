from lightgbm import LGBMRegressor

class LightGBMModel:
    _instance = None

    @staticmethod
    def get_instance():
        if LightGBMModel._instance is None:
            LightGBMModel()
        return LightGBMModel._instance

    def __init__(self):
        if LightGBMModel._instance is not None:
            raise Exception("This class is a singleton!")
        else:
            LightGBMModel._instance = self
            self.model = LGBMRegressor()

    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)
        return self.model

    def predict(self, X_test):
        return self.model.predict(X_test)
