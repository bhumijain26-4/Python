# Write a Python program to handle multiple exceptions (e.g., file not found, division by zero).

try:

    num1 = int(input("Enter a number : "))
    num2 = int(input("Enter a number : "))

    ans = num1 / num2
    print(ans)

    with open("myfile3.txt","r") as file:
         print(file.read())


except FileNotFoundError:
    print("File does not exists!")

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Invalid input!")

except Exception as e:
    print(e)
