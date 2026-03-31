import pandas as pd

input_path = "input.csv"
output_path = "result.csv"
sample = pd.DataFrame(
    {
        "name": ["Alice", "Bob", "Charlie"],
        "score": [85, 92, 78],
    }
)
sample.to_csv(input_path, index=False, encoding="utf-8")
data = pd.read_csv(input_path, encoding="utf-8")
data.to_csv(output_path, header=True, index=False, encoding="utf-8")

print(data)
