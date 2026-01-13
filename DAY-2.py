# x = 7
# y = 22
#
# if x <= 0 or y >= 20:
#     print(False)
# else:
#     print(True)


# from http.cookiejar import uppercase_escaped_char
#
# students = ["Ashray", "Dino", "Kalyan", "Uday", "Yash"]
# for student in students:
#     print(student)
#
#
# word = "heLLo PyTHon"
# for letter in word:
#     print(letter.upper())
#
# marks= int(input("Enter the integer marks: "))
# if marks >= 90:
#     print("Grade: A")
# elif marks >= 80:
#     print("Grade: B")
# elif marks >= 70:
#     print("Grade: C")
# elif marks >= 60:
#     print("Grade: D")
# else : print("Grade: F")

secret_number = 7
guess = 0
while guess != secret_number :
        guess = int(input("Guess the Secret Number(1-10): "))
        if guess < secret_number :
            print("Too Low!")
        elif guess > secret_number :
            print("Too High!")
print("Congratulations! You guessed the secret number!")