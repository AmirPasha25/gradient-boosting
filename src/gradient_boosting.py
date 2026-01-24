import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import make_regression

# Creating a synthetic dataset
class SyntheticData:
    def __init__(self, n_samples = 100, n_features = 1, n_targets = 1, random_state = 42, noise = 80):

        X,y = make_regression(n_samples = n_samples, n_features = n_features, n_targets = n_targets, random_state = random_state, noise = noise)
        df_x = pd.DataFrame(X, columns=[f"Column_{i}" for i in range(n_features)])
        df_y = pd.DataFrame(y, columns=[f"Target_{i}" for i in range(n_targets)])
        self.df = pd.concat((df_x, df_y), axis= 1)
    
    def dataframe(self):
        return self.df