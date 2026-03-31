import pandas as pd
from sklearn.datasets import load_iris
from ydata_profiling import ProfileReport

iris = load_iris()
iris = pd.DataFrame(iris.data, columns=iris.feature_names)
iris['Class'] = load_iris().target
iris['Class'] = iris['Class'].map({0: 'Setosa', 1: 'Versicolour', 2: 'Virginica'})

report = ProfileReport(iris, title="Iris Profiling Report")
report.to_file("iris_profile_report.html")
print("saved: iris_profile_report.html")

