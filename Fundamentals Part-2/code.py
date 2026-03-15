# age = int(input("Enter your age: "))
# if age >= 18:
#     print("You can vote!")
#     print("You can drive!")
# else:
#     print("You can't vote")
#     print("You can't drive")

# color = input("Enter a color: ")
# if color == "red" or color == "Red":
#     print("Stop!")
# elif color == "yellow":
#     print("Get ready!")
# elif color == "green":
#     print("Go!")
# else:
#     print("Wrong color for traffic lights!")

# age = int(input("Enter your age: "))
# if age < 13:
#     print("You are a child.")
# elif age >= 13 and age < 18:
#     print("You are a teenager.")
# else:
#     print("You are an adult.")

# username = input("Enter your username: ")
# password = input("Enter your password: ")
# if (username == "admin" and password == "pass"):
#     print("Login Successfull!!")
# elif (username != "admin"):
#     print("Wrong Username")
# else:
#     print("Wrong Password")

# n = int(input("Enter the number: "))
# if n % 5 == 0:
#     print(n, "is multiple of 5")
# else:
#     print(n, "is not multiple by 5")

# num = int(input("Enter the number: "))
# if (num % 2 == 0):
#     print(num, "is even number")
# else:
#     print(num, "is odd number")

# Nesting
# username = input("Enter your username: ")
# password = input("Enter your password: ")
# if (username == "admin" and password == "pass"):
#     print("Login Successfull!!")
# else:
#     if (username != "admin"):
#         print("Wrong username")
#     else:
#         print("Wrong password")

# color = input("Enter color: ")
# match color:
#     case "Green":
#         print("Go")
#     case "Yellow":
#         print("Look")
#     case "Red":
#         print("Stop")
#     case _: # Default Cases
#         print("Wrong color!!")

# infinte loop
# while True:
#     print("Hello World!!")

# finite loop => prints Hello World!! 5x
# count = 1 # iterator
# while count <= 10:
#     print("Hello World!!", count)
#     count += 1
# print("After loop, Count =", count)

# 1 to 5
# i = 1
# while i <= 5:
#     print(i)
#     i += 1

# 5 to 1
# i = 5
# while i >= 1:
#     print(i)
#     i -= 1

# Print multiplication table of any number entered by the user
# j = int(input("Enter the number to get the table: "))
# i = 1
# while i <= 10:
#     print(j, "x", i, "=", i * j)
#     i += 1

# break keyword
# i = 1
# while i <= 10:
#     if i % 6 == 0:
#         break
#     print(i)
#     i += 1
# print("Outside the loop now")

# continue keyword
# i = 1
# while i <= 10:
#     if i % 3 == 0:
#         i += 1
#         continue
#     print(i)
#     i += 1
# print("Outside the loop now...")

#print all the odd number from 1 to 10
# i = 1
# while i <= 10:
#     if i % 2 != 0:
#         print(i)
#     i += 1

# odd numbers
# i = 1 
# while i <= 10:
#     print(i)
#     i += 2

# print odd numbers using continue keyword
# i = 1
# while i <= 10:
#     if i % 2 == 0:
#         i += 1
#         continue
#     print(i)
#     i += 1

# i = 0
# while i < 10:
#     i += 1
#     if i % 2 == 0:
#         continue
#     print(i)

# even numbers
# i = 2 
# while i <= 10:
#     print(i)
#     i += 2

# for loop
# string = "Hello"
# if 'o' in string:
#     print("o exists in string")
# for var in string: # in -> membership operator => check value presence
#     print(var)

# for i in range (5):
#     # print(i+1)
#     print("Hello World")

# word = "artificial intelligence"
# count = 0
# for ch in word:
#     if ch == 'i':
#         count += 1
# print("count of i =", count)

# Print vowel count of a given string
# word = "rishabh sahan jain"
# count = 0
# for ch in word:
#     if ch in "aeiou":
#         count += 1
# print("Vowel count =", count)

# word = "artificial intelligence"
# count = 0
# for ch in word:
#     if ch == 'a' or ch == 'e' or ch == 'i' or ch =='o' or ch == 'u':
#         count += 1
# print("Vowel count =", count)

# range()
