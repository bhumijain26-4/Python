# Write a Python program to create a calculator using functions.

def add(x,y):
    return x + y
def sub(x,y):
    return x - y
def mul(x,y):
    return x * y
def div(x,y):
    return x / y

print("Choose any operator : +,-,*,/")
choice = input("Enter any operator : ")
num1 = float(input("Enter first value : "))
num2 = float(input("Enter second value : "))

if choice == '+':
    result = add(num1,num2)
elif choice == '-':
    result = sub(num1,num2)
elif choice == '*':
    result = mul(num1,num2)
elif choice == '/':
    result = div(num1,num2)
else:
    print("Invalid Input!!")
print("Output is : ",result)
