"""
Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.
"""

num1 = int(input("Enter the value of num1: "))
num2 = int(input("Enter the value of num2: "))
num3 = int(input("Enter the value of num3: "))

sum = num1 + num2 + num3

if num1 == num2 or num2 == num3 or num1 == num3:
   print("The sum is : 0")
else:
    print(f"The sum of 3 Integers is : {sum}")
    
