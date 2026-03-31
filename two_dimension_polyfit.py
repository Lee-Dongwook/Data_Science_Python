import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

iris_load = load_iris()
iris = pd.DataFrame(iris_load.data, columns=iris_load.feature_names)
iris['class'] = load_iris().target
iris['class'] = iris['class'].map({0: 'Setosa', 1: 'Versicolour', 2: 'Virginica'})

iris_2 = iris.sort_values(by='sepal length (cm)')
X, Y = iris_2['sepal length (cm)'], iris_2['petal length (cm)']

b2, b1, b0 = np.polyfit(X, Y, 2)

def quadratic_func(x):
    return b0 + b1 * x + b2 * x ** 2

plt.scatter(x = X, y = Y, alpha = 0.5)
plt.plot(X, quadratic_func(X), c='red')
plt.show()
