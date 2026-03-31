from sklearn.datasets import load_iris
import pandas as pd

iris = load_iris()
iris = pd.DataFrame(iris.data, columns=iris.feature_names)

print(iris[1:4])

iris_ex_header = 'sepal length (cm)'
print(iris[iris_ex_header].head(4))

iris_ex_column = ['sepal length (cm)', 'sepal width (cm)']
print(iris[iris_ex_column].head(4))

iris_ex_row_column = [1, 2]
print(iris.iloc[iris_ex_row_column].head(4))

iris_ex_row_column = [1, 2]
print(iris.iloc[iris_ex_row_column].head(4))

