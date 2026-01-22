import pandas as pd

# in terminal type pip install pandas  or python -m install pandas

# ages = pd.Series((18,21,24))
# # print(ages)
#
#
# data = {
#     "name" : ["Alice", "Bob", "Charlie"],
#     "age" :  [20, 22, 19],
#     "score" : [85, 90, 88]
# }
#
# df = pd.DataFrame(data)
# # print(df["score"][0])
#
# # print(df.head(2))
# # print(df.tail(2))
#
# # print(df.info())
# # print(df.head())
# # print(df.describe())
#
# print(df.isnull().sum())
# print(df.dropna())
# print(df.values.shape)



# df = pd.read_json("C:\\Users\\ashri\\Downloads\\students.json")

# print(df.head(10))
# print(df.shape)
# print(df.describe())
# print(df.dtypes)
# print(df.info())
# print(df.isnull().sum())
# print(df.dropna(how='all').sum())
# print(df.fillna(df.isnull().mean()))

# df["student_id"] = pd.to_numeric(df["student_id"])
# df["student_id"] = df["student_id"].astype(str)

# print(df.info())
# print(df.head())

# print(df.drop_duplicates())
# print(df[df["age"]>22])
# print(df[["name", "marks", "gender"]])
# print(df.sort_values(by=['age'], ascending=False).head(10))

# print(df.groupby("age")["gender"].sum())

# print(pd.get_dummies(df))
# print(pd.merge(left_on="student_id", right_on="student_id", how="inner"))


# print(len(df))

# print(df.iloc[9])
# print(df.isnull().sum())
# df.fillna(df.mean(), inplace=True)
# df.fillna(df.mean(numeric_only=True), inplace=True)
# print(df)
# df.to_json("C:\\Users\\ashri\\Downloads\\students.json.gz")
