import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import make_regression

X,y = make_regression(n_samples = 10, n_features = 4, n_targets = 1, random_state = 42, noise = 80)
df_x = pd.DataFrame(X, columns=[f"Column_{i}" for i in range(4)])
df_y = pd.DataFrame(y, columns=[f"Target_{i}" for i in range(1)])
print(df_x)