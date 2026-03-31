import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
from sklearn.datasets import load_iris
import seaborn as sns

iris = load_iris()
iris = pd.DataFrame(iris.data, columns=iris.feature_names)
iris['Class'] = load_iris().target
iris['Class'] = iris['Class'].map({0: 'Setosa', 1: 'Versicolour', 2: 'Virginica'})

scatter_matrix(iris, alpha = 0.5, figsize = (8, 8), diagonal = 'hist')
plt.show()

sns.pairplot(iris, diag_kind='auto', hue = 'Class')
plt.show()
