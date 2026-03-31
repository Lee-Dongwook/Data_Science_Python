import pandas as pd
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

iris = load_iris()
iris = pd.DataFrame(iris.data, columns=iris.feature_names)
iris['class'] = load_iris().target
iris['class'] = iris['class'].map({0: 'Setosa', 1: 'Versicolour', 2: 'Virginica'})

plt.boxplot(iris.drop(columns='class'))
plt.xlabel('Features')
plt.ylabel('Value')
plt.title('Box Plot of Iris Dataset')
plt.show()
