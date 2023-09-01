import numpy as np
from sklearn.ensemble import RandomForestRegressor

N = 10000
p = 0.1
X_train = np.random.choice(a=[0, 1], size=(N, 56), p=[p, 1-p])


print(X_train)


rf = RandomForestRegressor()
