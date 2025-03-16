"""
Write python program that swap two number with temp variable and without temp variable. 
"""

#Using temp v   ariable
num1 = int(input("Enter the value of num1: "))
num2 = int(input("Enter the value of num2: "))

print(f"Before Swapping : {num1} {num2}",end="")

temp = num1
num1 = num2
num2 = temp

print(f"\nAfter Swapping : {num1} {num2}",end="")

#Without temp variable

num1 = int(input("\n\nEnter the value of num1: "))
num2 = int(input("Enter the value of num2: "))

print(f"Before Swapping : {num1} {num2}",end="")

num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2

print(f"\nAfter Swapping : {num1} {num2}",end="")
