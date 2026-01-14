# # Personal Information
# name = "Ashray"
# age = 24
# favorite_number = 7
#
# print(f"My name is {name}, I am {age} years old, and my favorite number is {favorite_number}.")
#
#
# # Simple Calculations
# num1 = 10
# num2 = 5
#
# print("Sum:", num1 + num2)
# print("Difference:", num1 - num2)
# print("Product:", num1 * num2)
#
#
# # Student Profile
# student_name = "John"
# grade = "A"
# age = 16
#
# print(f"Student Name: {student_name}, Grade: {grade}, Age: {age}")
#
#
# # Shopping Bill Calculator
# item1_price = 14.99
# item2_price = 10.00
# item3_price = 4.99
#
# items_total = item1_price + item2_price + item3_price
# total_bill = items_total * 1.08
# print(f"Total Bill Amount: ${total_bill:.2f}")

#
# # Loop Practice
# # Counting Numbers
# print("Counting Numbers:")
# for i in range(1, 11):
#     print(i)
#
# # Even Numbers (1 to 20)
# print("Printing the Even Numbers B/W 1-20:")
# for i in range(1, 21):
#     if i % 2 == 0:
#         print(i)


# # Multiplication Table
# number = int(input("Enter a number: "))
#
# print(f"Multiplication Table for {number}:\n")
# for i in range(1, 11):
#     print(f"{number} x {i} = {number * i}")

#
# # Daily Step Counter
# steps = [5000, 6200, 4500, 7000, 8000, 6000, 7500]
#
# print("Daily Step Counter:\n")
# for day in range(1, 8):
#     print(f"Day {day}: {steps[day - 1]} steps")

#
# # Classroom Attendance
# print("Classroom Attendance:\n")
#
# for student in range(1, 11):
#     # Condition: even student numbers are present
#     if student % 2 == 0:
#         status = "Present"
#     else:
#         status = "Absent"
#     print(f"Student {student}: {status}")

#
# # Multiplication Table (Shop Prices)
# price = float(input("Enter the price of one item: "))
#
# print(f"\nTotal cost for multiple quantities:\n")
#
# for quantity in range(1, 11):
#     total = price * quantity
#     print(f"{quantity} items: ${total:.2f}")