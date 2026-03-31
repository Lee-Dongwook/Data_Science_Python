import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris_load = load_iris()
iris = pd.DataFrame(iris_load.data, columns=iris_load.feature_names)
iris['class'] = load_iris().target
iris['class'] = iris['class'].map({0: 'Setosa', 1: 'Versicolour', 2: 'Virginica'})

def linear_func(x):
    return 2 * x + 1

X = iris['sepal length (cm)']
plt.plot(X, linear_func(X), c='red')
plt.show()
