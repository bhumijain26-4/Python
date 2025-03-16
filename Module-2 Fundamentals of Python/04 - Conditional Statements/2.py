"""
Write a Python program to check if a number is prime using if_else.
"""
num = int(input("Enter a number: "))

if num > 1:
    if num == 2 or num == 3:
        print(f"{num} is a prime number")
    elif num % 2 == 0 or num % 3 == 0:
        print(f"{num} is not a prime number")
    else:
        print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")
