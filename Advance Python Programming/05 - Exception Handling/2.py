# Write a Python program to demonstrate handling multiple exceptions.
try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a number: "))

    result = num1/num2

    print(result)

    list = [1,2,3,4,5]
    print(list[6])
    
except ZeroDivisionError:
    print("Cannot divide by zero")

except IndexError:
    print("This index does not exist")

except ValueError:
    print("Invalid input!")
