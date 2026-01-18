# Active batch job
# Active batch jobs are written on databricks
# S3,> Glue jobs,> AWS Lambda,> Postgres

# python script to format the data and put it into the

# with open("C:\\Users\\ashri\\OneDrive\\Desktop\\Homework_1-15.txt", "r") as file:
#     content = file.read()
#     print(content.strip().title())

#
#
# with open("C:\\Users\\ashri\\OneDrive\\Desktop\\Homework_1-15.txt", "w") as file:
#     content = file.write("\n Added a new content \n ")
#     new_content = file.write("\n Added a one more line \n ")

import csv
import pandas as pd

df = pd.read_csv("C:\\Users\\ashri\\Downloads\\student_data.csv")
print(df.head(10))
# print(df.tail(1))
# print(df.info())


# with open("C:\\Users\\ashri\\Downloads\\student_data.csv", "r") as file:
#     reader = csv.reader(file)
#     for n in reader:
#         print(n)

with open("C:\\Users\\ashri\\Downloads\\student_data.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)


with open("C:\\Users\\ashri\\Downloads\\student_data.csv", "w") as file:
    write = csv.writer(file)
    write.writerows(["111", "John", "24", "M", "Data Engineer", 97])
