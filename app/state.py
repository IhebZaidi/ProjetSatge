# app/state.py
import pandas as pd

class State:
    def __init__(self):
        self.uploaded_df: pd.DataFrame = None

state = State()
