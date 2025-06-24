# Write a Python program to handle exceptions in a calculator.

try:
    num1 = float(input("Enter number 1 : "))
    num2 = float(input("Enter number 2 : "))

    operation = input("Enter operator (+,-,*,/) : ")
    
    if operation == '+':
        ans = num1 + num2
    elif operation == '-':
        ans = num1 - num2
    elif operation == '*':
        ans = num1 * num2
    elif operation == '/':
        ans = num1/num2
    
    print(ans)

except ZeroDivisionError:
    print("Cannot Divide by zero")
except ValueError:
    print("Invalid Input")
