# def cube (x):
#     return x*x*x
#
# print(cube(5))


# def greet_student(name,score):
#     # return print(f" Hello {name},\n Your score is {score},\n Good Job! ")
#         print("Hello", name)
#         print ("Your score is", score)
#         if score >= 80:
#             print("Excellent work!")
#         elif score >= 70:
#             print("Good work!")
#         else:
#             print("Need to work Hard!")

# greet_student("Alice", 47)


# list= ["Ashray", "John", "Jane", "Keith"]
#
# def greet (name):
#     print("Hello " + name +"!")
#
#
# for i in range(len(list)):
#     greet(list[i])
#
#
# def add_numbers(*args):
#     return sum(args)
#
# print(add_numbers(1,2,3,4,5,6))


def create_user_profile(**kwargs):
    profile = {}
    for key,value in kwargs.items():
        profile[key] = value
    return profile

user_1 = create_user_profile( name= "Ashray", age = 24, Location = "Knoxville")
user_2 = create_user_profile( name= "Janice", profession = "Engineer", Location = "New York")
user_3 = create_user_profile( name= "Janice", profession = "Engineer")

print(user_1)
print(user_2)
print(user_3)





