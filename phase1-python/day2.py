#Arithmetic Operators
# a = float(input("Enter number a: "))
# b = float(input("Enter number b: "))

# print(a + b)   # Addition
# print(a - b)   # Subtraction
# print(a * b)   # Multiplication
# print(a / b)   # Division
# print(a // b)  # Floor Division
# print(a % b)   # Modulus (Remainder)
# print(a ** b)  # Exponent



# Comparison Operators
# a = float(input("Enter number a: "))
# b = float(input("Enter number b: "))

# print(a == b)  # Equal
# print(a != b)  # Not Equal
# print(a > b)   # Greater Than
# print(a < b)   # Less Than
# print(a >= b)  # Greater Than or Equal
# print(a <= b)  # Less Than or Equal

#String Operations
# def format_my_text(text): #Global function to format text
#     #Remove blank spaces and ensure it's a string
#     cleaned_text = str(text).strip()
    
#     #Capitalize the first letter of each word
#     final_text = cleaned_text.title()
    
#     return final_text

# First_name = format_my_text(input("Enter your first name: "))
# Last_name = format_my_text(input("Enter your last name: "))

# print("My name is " + First_name + " " + Last_name)

# #Length of the string
# print("The length of your first name is:", len(First_name))

#Using if-else statements
# age = int(input("Enter your age: "))
# if age >= 18:
#     print("You are an adult.")
# else:
#     print("You are a minor.")



#Simple grade checker
grade = float(input("Enter your grade: "))
if grade >= 90:
     print("You got an A!")
elif grade >= 80:
    print("You got a B.")
elif grade >= 70:
    print("You got a C.")
elif grade >= 60:
    print("You got a D.")
elif grade >= 50 and grade <= 59:
    print("You got an F.")
else:
    print("You need to improve.")


#Password checker
password = input("Enter your password: ")
if password == "password123":
    print("Access granted!")
else:
    print("Access denied.")