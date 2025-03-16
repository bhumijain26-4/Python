"""
Write a Python program to find a specific string in the list using a simple
for loop and if condition.
"""
list1 = ["python","php","flutter","java","Reactjs"]

for course in list1:
    if course == "python":
        print("Python is found")
    elif course == "php" :
        print("Php is found")
    elif course == "flutter" :
        print("Flutter is found")
    elif course == "java":
        print("Java is found")
    else :
        print(f"{course} is Invalid option!")