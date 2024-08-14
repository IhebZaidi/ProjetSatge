import pandas as pd

class State:
    _instance = None

    @staticmethod
    def get_instance():
        if State._instance is None:
            State()
        return State._instance

    def __init__(self):
        if State._instance is not None:
            raise Exception("This class is a singleton!")
        else:
            State._instance = self
            self.uploaded_df: pd.DataFrame = None

# Initialisation de l'instance unique
state = State.get_instance()
