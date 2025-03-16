"""
Write a Python program to get the Factorial number of given number. 
"""
fact = 1
num = int(input("Enter any number: "))
for i in range(1,num+1):
  fact = fact*i
print("The Factorial of given number is : ",end="")
print(fact)