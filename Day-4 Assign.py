# Scenario (Real-World Inspired)
#
# A company receives raw daily sales data from a store.
# Before analytics can use it, the data must go through multiple
# pipeline steps, where each function passes its output to the next.
# This is exactly how ETL pipelines work.




# def extract_sales():
#     user_input = input("Enter sales values separated by commas: ")
#     # sales = user_input.split(",")
#
#     sales_list = [float(x.strip())for x in user_input.split(",")]
#     #
#     # sales_list = []
#     # # sales_list = [100, 250, 0, -50, 300, 150, -150, 0]
#     # for value in sales:
#     #     sales_list.append(float(value))
#
#
#
#     return sales_list
#
# def clean_sales(sales_list):
#     cleaned_sales = []
#     for sale in sales_list:
#         if sale != None and sale >0:
#             cleaned_sales.append(sale)
#
#     return cleaned_sales
#
# def transform_sales(cleaned_sales):
#     transformed_sales = []
# # Transforms sales amounts to include 10% tax
#     for sale in cleaned_sales:
#         transformed_sales.append(round(sale * 1.10, 2))
#     return transformed_sales
#
# def load_sales(final_sales):
#     total_sales = sum(final_sales)
#     average_sales = total_sales / len(final_sales)
#
#     print("Final Sales Data:", final_sales)
#     print("Total Sales:", total_sales)
#     print("Average Sales:", average_sales)
#
#
# raw_data = extract_sales()
# cleaned_data = clean_sales(raw_data)
# transformed_data = transform_sales(cleaned_data)
# load_sales(transformed_data)


# 2 build a func to do the arithmetic operations on multiple argument inputs.

# def arithmetic_operations(*args):
#     total = sum(args)
#
#     difference = args[0]
#     for num in args[1:]:
#         difference -= num
#
#     product = 1
#     for num in args:
#         product *= num
#
#     average = total / len(args)
#
#     return total, difference,product, average
#
#
# user_input = input("Enter numbers separated by commas: ")
# args = [float(x.strip()) for x in user_input.split(",")]
#
#
# result = arithmetic_operations(*args)
#
# print("Sum:", result[0])
# print("Difference:", result[1])
# print("Product:", result[2])
# print("Average:", result[3])



# Exercise PYTHON FUNCTIONS
# Lambda, map, reduce and filter funcs
#
# Question
# Convert all temperatures to Fahrenheit.
#
# temps_c = [0, 10, 20, 30]
#
# temps_f = list(map(lambda x: (x* 9/5) + 32, temps_c))
#
# print(temps_f)
#
# # Question
# # Keep only transactions with amount > 0.
# transactions = [100, -20, 300, 0, -5, 450]
#
# cleaned = list(filter(lambda amount: amount > 0, transactions))
# print(cleaned)
#
# # Question
# # Compute total revenue.
#
# orders = [120, 340, 560, 80]
#
# from functools import reduce
#
# total= reduce(lambda x, y: x + y, orders)
# # total = sum(orders)
#
# print(total)
#
# # Question: Apply a 10% discount only to orders above $500.
# # Return discounted values.
#
# orders = [100, 250, 600, 800, 120]
#
# filtered = list(filter(lambda amount: amount > 500, orders))
# discounted_total = list(map(lambda amount: amount *0.90, filtered))
# print(discounted_total)
#
# discounted = list(map(lambda x : x * 0.9, filter(lambda amount: amount > 500, orders)))
# print(discounted)
#
#
# # Question
# # Extract only users with valid email IDs.
#
# users = [
#     {"name": "A", "email": "a@gmail.com"},
#     {"name": "B", "email": None},
#     {"name": "C", "email": "c@yahoo.com"}
# ]
#
# cleaned = list(map(lambda x: x, filter(lambda u:u["email"] != None, users)))
# print(cleaned)
#
# # Optimal solution by GPT
# valid_users = list(filter(lambda u: u["email"], users))
# print(valid_users)
#
# # Question
# # Find total items sold.
#
# orders = [
#     {"items": 4},
#     {"items": 7},
#     {"items": 2}
# ]
#
# total_items = reduce(lambda acc, y: acc + y["items"], orders, 0)
# print(total_items)
#
#
# # Return cleaned names.
#
# names = ["  alice ", "BOB", " ChaRLie "]
#
# clean_names = list(map(lambda n: n.strip().title(), names))
# print(clean_names)
#

############
# Few Example Problems on *args and **kwargs:

# def load_config(**config):
#     return {
#         "host": config.get("host", "localhost"),
#         "port": config.get("port", 5432),
#         "debug": config.get("debug", False)
#     }
#
# print(load_config(host="db.prod", debug=True))
# print(load_config(port= 191875))
#
# # Problem: Ensure name exists in keyword arguments.
#
# def create_user(**kwargs):
#     if "name" not in kwargs:
#         raise ValueError("Name is required")
#     return kwargs
#
# print(create_user(name="Bob", age=28))

# def validate_record(record, *rules, **options):
#     for rule in rules:
#         if not rule(record):
#             return False
#     return options.get("strict", True)
#
# validate_record(data,is_not_null,is_positive,strict=False)
#
#
# user = {"name": "Ashray", "role": "DE"}
# print(**user)

# def log_metric(metric_name, *values, **tags):
#     print("Metric:", metric_name)
#     print("Values:", values)
#     print("Tags:", tags)
#
# log_metric("cpu_usage", 75, 80, host="server1", region="us-east")
#
# def apply_discount(discount, *orders):
#     return [order * (1 - discount) for order in orders]
#
# print(apply_discount(0.1, 100, 200, 300))

