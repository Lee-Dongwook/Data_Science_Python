import pandas as pd

score = pd.DataFrame({'국어': [90, 85, 95], '영어': [95, 80, 85], '수학': [85, 90, 95]}, index=['장화','홍련','주디'])

score.loc['홍련','영어'] = 100

print(score)

score['국어'] = score['국어'] - 10
print(score)
