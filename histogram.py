import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine

wine_load = load_wine()
wine = pd.DataFrame(wine_load.data, columns=wine_load.feature_names)
wine['Class'] = wine_load.target
wine['Class'] = wine['Class'].map({0: 'class_0', 1: 'class_1', 2: 'class_2'})

wine_type = wine['Class'].value_counts()
print(wine_type)

plt.hist('alcohol', bins=8, range=(11,15), color='purple', data=wine)
plt.xlabel('Alcohol')
plt.ylabel('Count')
plt.title('Wine Alcohol Count')
plt.show()
