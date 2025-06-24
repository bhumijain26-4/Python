# Write a Python program to show single inheritance. 

class A:
    def display(self):
        print("This is the parent class")

class B(A):
    def displayB(self):
        print("This is the child class")


obj = B()
obj.display()
obj.displayB()