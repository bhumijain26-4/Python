# Write a Python program to print custom exceptions.

class mycustom(Exception):
    pass


def check_positive(number):
    if number < 0:
        raise mycustom("Negative values are not allowed!!")
    
try:
    number = int(input("Enter a number : "))
    check_positive(number)
    print("The number is valid!")

except Exception as e:
    print(e)