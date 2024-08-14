from sklearn.ensemble import RandomForestRegressor

class RandomForestModel:
    _instance = None

    @staticmethod
    def get_instance():
        if RandomForestModel._instance is None:
            RandomForestModel()
        return RandomForestModel._instance

    def __init__(self):
        if RandomForestModel._instance is not None:
            raise Exception("This class is a singleton!")
        else:
            RandomForestModel._instance = self
            self.model = RandomForestRegressor()

    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)
        return self.model

    def predict(self, X_test):
        return self.model.predict(X_test)
