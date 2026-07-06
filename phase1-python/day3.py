#Importance of loops in programming

#for and while

# for i in range(5):
#     print("This is iteration number:", i)

# counter = 0
# while counter < 5:
#     print("This is iteration number:", counter)
#     counter += 1

#break and continue statements
# for i in range(10):
#     if i == 8:
#         break
#     print("This is iteration number:", i)

#count to 20
# for i in range(1,21):
#     print("This is iteration number:", i)

#Multiplication table
# num = int(input("Enter a number:"))
# for i in range(1,11):
#     print(num, "*", i, "=", num * i)


#Sum of numbers 1 to n
# n = int(input("Enter a number n:"))
# sum = 0
# for i in range(1, n + 1):
#     sum += i
# print("Sum of numbers from 1 to", n, "is:", sum)

#Guess the number game
n = int(input("Enter a number: "))
counter=0
while counter < 10:
    key = 5
    if n == key:
        print("Congratulation!",key, "is the right guess")
        break
    counter += 1
else:
    print("Try again!!")
        