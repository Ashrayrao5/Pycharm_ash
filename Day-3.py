# fruits = ["apple", "banana", "cherry"]
#
# fruits.insert(10, "Blueberry")
# print(fruits[3])

#
# list = [1,2,2,3,3,4,4,4,4,5,6,7,7,8,9]
# abc = set(list)
# print(abc)

#
# person = dict(name = 'John', age = 20, city = 'New York')
# print(person)


person_1 = {"name" :"John", "age" : 20, "city":'New York'}
print(person_1)

person_2 = {}
person_2["name"] = "Sarah"
person_2["age"] = 24
person_2["city"] = "Boston"
person_2["email"] ="abc.email.com"
print(person_2)

# Nested Dictionaries

# practice list, tuples, set and dict
# More work on syntax and other use cases

# Home-work
# Practice the Dictionaries
# insert
# delete

# Do any research on the API for data Analytics purposes


student = {
    "name": "John",
    "marks": {
        "math": 85,
        "science": 90,
        "english": 88
    }
}


print(student["name"])
print(student["marks"]["math"])


student["marks"]["math"] = 95
print(student["marks"])


for subject, score in student["marks"].items():
    print(subject, ":", score)


# 6-lvl Nested Dict

company_data = {
    "company": {
        "name": "TechCorp",
        "departments": {
            "IT": {
                "teams": {
                    "Data": {
                        "projects": {
                            "SalesAnalytics": {
                                "metrics": {
                                    "2026-01-10": {
                                        "revenue": 120000,
                                        "orders": 950
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}


revenue = company_data["company"] \
    ["departments"]["IT"] \
    ["teams"]["Data"] \
    ["projects"]["SalesAnalytics"] \
    ["metrics"]["2026-01-10"] \
    ["revenue"]

print(revenue)   # 120000


# Updating a Value
company_data["company"]["departments"]["IT"]["teams"]["Data"] \
["projects"]["SalesAnalytics"]["metrics"]["2026-01-10"]["orders"] = 1000


# Adding a New Metric
company_data["company"]["departments"]["IT"]["teams"]["Data"] \
["projects"]["SalesAnalytics"]["metrics"]["2026-01-11"] = {
    "revenue": 130000,
    "orders": 980
}