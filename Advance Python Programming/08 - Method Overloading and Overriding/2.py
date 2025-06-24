#  Write a Python program to show method overriding.

class A:
    def display(self):
        print("A class is here")

class B(A):
    def display(self):
       super().display()
       print("B class is here")

obj = B()
obj.display()