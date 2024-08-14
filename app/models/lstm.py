import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.optimizers import Adam

class LSTMModel:
    _instance = None

    @staticmethod
    def get_instance():
        if LSTMModel._instance is None:
            LSTMModel()
        return LSTMModel._instance

    def __init__(self):
        if LSTMModel._instance is not None:
            raise Exception("This class is a singleton!")
        else:
            LSTMModel._instance = self
            self.model = Sequential()
            self.model.add(LSTM(50, activation='relu', input_shape=(None, 1)))
            self.model.add(Dense(1))
            self.model.compile(optimizer=Adam(learning_rate=0.001), loss='mse')

    def train(self, X_train, y_train):
        X_train_lstm = np.array(X_train).reshape((X_train.shape[0], X_train.shape[1], 1))
        self.model.fit(X_train_lstm, y_train, epochs=20, batch_size=32, verbose=1, validation_split=0.2)
        return self.model

    def predict(self, X_test):
        X_test_lstm = np.array(X_test).reshape((X_test.shape[0], X_test.shape[1], 1))
        return self.model.predict(X_test_lstm).flatten()
