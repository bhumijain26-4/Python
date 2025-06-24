# Write a Python program to create a class and access the properties of the class using an object.
class User:
    def __init__(self,name,age):
        self.name = name
        self.age =  age

    def display(self):
        print("Name : {self.name}")
        print("Age : {self.age}")
obj = User()

obj.display()
