"""
Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.
"""

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
 
if a == b:
   result = True
elif a + b == 5:
   result = True
elif a - b == 5:
   result = True
else:
   result = False

print(f"The result of two Integers is : {result}")


     
