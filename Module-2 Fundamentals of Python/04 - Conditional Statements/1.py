"""
Write a Python program to find greater and less than a number using if_else.
"""
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

if a > b:
    print(f"{a} is Greater than {b}",end = "")
elif a < b:
    print(f"{a} is less than {b}",end = "")
else : 
    print(f"{a} is equal to {b}")

