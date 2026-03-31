# Data_Science_Python

`scikit-learn`의 Iris 데이터셋을 사용해 기본적인 데이터 탐색(EDA)과 시각화, 다항 회귀 피팅을 연습하는 파이썬 예제 프로젝트입니다.

## 프로젝트 개요

이 저장소는 다음 내용을 빠르게 실습할 수 있도록 구성되어 있습니다.

- Iris 데이터셋 로드 및 클래스 라벨 매핑
- 산점도(Scatter Plot) 시각화
- 산점도 행렬(Scatter Matrix) 및 Pair Plot 시각화
- 상관계수(피어슨) 히트맵 시각화
- 1차/2차 다항식 피팅(`numpy.polyfit`)
- `ydata-profiling` 기반 자동 EDA 리포트 생성

## 실행 환경

- Python 3.9 이상 권장
- 주요 라이브러리
  - `pandas`
  - `numpy`
  - `matplotlib`
  - `seaborn`
  - `scikit-learn`
  - `ydata-profiling`

설치 예시:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn ydata-profiling
```

## 파일 설명

- `scatter_plot.py`  
  붓꽃의 `sepal length`와 `sepal width`를 클래스별 색상/스타일로 산점도 시각화합니다.

- `scatter_matrix.py`  
  `pandas.plotting.scatter_matrix`와 `seaborn.pairplot`으로 변수 간 관계를 한 번에 확인합니다.

- `heatmap.py`  
  수치형 변수들 간 피어슨 상관계수를 계산하고 히트맵으로 표현합니다.

- `polyfit.py`  
  `sepal length`(X)와 `petal length`(Y) 관계를 1차 선형식으로 피팅해 산점도 위에 회귀선을 그립니다.

- `two_dimension_polyfit.py`  
  동일 변수 조합을 2차 다항식으로 피팅해 곡선 형태 관계를 시각화합니다.

- `_pandas_profiling.py`  
  Iris 데이터 전체에 대한 프로파일 리포트를 생성하고 `iris_profile_report.html` 파일로 저장합니다.

- `iris_profile_report.html`  
  생성된 EDA 결과물(HTML 리포트)입니다.

## 실행 방법

프로젝트 루트에서 원하는 스크립트를 실행하면 됩니다.

```bash
python scatter_plot.py
python scatter_matrix.py
python heatmap.py
python polyfit.py
python two_dimension_polyfit.py
python _pandas_profiling.py
```

## 참고 사항

- 각 스크립트는 독립 실행형이라 서로 의존하지 않습니다.
- 시각화 스크립트는 실행 시 그래프 창(`matplotlib`)이 열립니다.
- 프로파일링 스크립트 실행 후 생성되는 `iris_profile_report.html`은 브라우저에서 열어 상세 분석 결과를 확인할 수 있습니다.
