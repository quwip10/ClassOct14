# pip install pandas
from pandas import DataFrame

df = DataFrame(
    data={"length": [34, 45, 22, 87, 90], "width": [15, 67, 100, 50, 7]})

print(df)
print()
print(df.values)
print()
print(df.describe())


column = "length"

col_max = df[column].max()
col_min = df[column].min()

print(col_max, col_min)
