import pandas as pd
from sklearn.datasets import load_iris
import seaborn as sns
import matplotlib.pyplot as plt

iris_load = load_iris()
iris = pd.DataFrame(iris_load.data, columns=iris_load.feature_names)
iris['Class'] = load_iris().target
iris['Class'] = iris['Class'].map({0: 'Setosa', 1: 'Versicolour', 2: 'Virginica'})


iris_corr = iris.drop(columns='Class').corr(method='pearson')
sns.heatmap(iris_corr, xticklabels=iris_corr.columns, yticklabels=iris_corr.columns, cmap='RdBu_r', annot=True)
plt.show()
