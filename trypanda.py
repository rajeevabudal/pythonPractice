import pandas as pd

data = pd.read_xlsx("/Users/rajeevabudal/Downloads/2318083-car_data.xlsx")

# print(data.head())
# print(data[["name", "sex"]].head())
# print(data[data.name == "na"].head())
# # print(data.tail(1))
# print(data.shape[0])

# print(list(data.columns))

# print(type(data))

# print(data[(data["name"] == "Max Ruin ") & (data["mark"] == 85)].head())

# print(data[data["mark"].isin ([60, 75])]).head(5)

print(data.dtypes)
