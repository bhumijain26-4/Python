"""
Write a Python program to calculate grades based on percentage using if-else ladder
"""
percentage = float(input("Enter your percentage: "))

if percentage >= 90 :
    print("Your Grade is A+")
elif percentage >= 80 :
   print("Your Grade is A")
elif percentage >= 70 :
    print("Your Grade is B")
elif percentage >= 60 :
    print("Your Grade is C")
elif percentage >= 50 :
    print("Your Grade is D")
else :
    print("Fail")
