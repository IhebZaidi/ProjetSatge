from xgboost import XGBRegressor

class XGBoostModel:
    _instance = None

    @staticmethod
    def get_instance():
        if XGBoostModel._instance is None:
            XGBoostModel()
        return XGBoostModel._instance

    def __init__(self):
        if XGBoostModel._instance is not None:
            raise Exception("This class is a singleton!")
        else:
            XGBoostModel._instance = self
            self.model = XGBRegressor()

    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)
        return self.model

    def predict(self, X_test):
        return self.model.predict(X_test)
