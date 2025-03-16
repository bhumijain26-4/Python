"""
Write a Python program to check if a person is eligible to donate blood using a nested if.
"""
age = int(input("Enter your age: "))
weight = float(input("Enter you weight (in kgs): "))

if age >= 18:
    if weight >= 50:
        print("You are eligible to donate blood")
    else : 
        print("You are not eligible to donate blood due to weight.")
else:
    print("You are not eligible to donate blood due to age.")