import numpy as np
import pandas as pd

dataset = np.array([['kor', 70], ['math', None]], dtype=object)
df = pd.DataFrame(dataset, columns=['class', 'score'])

print(df)
