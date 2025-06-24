# Write a Python program to show multilevel inheritance.

class A:
    def display(self):
        print("This is the parent class")

class B(A):
    def displayB(A):
        print("This is the child-1 class")
    
class C(B):
    def displayC(B):
        print("This is the child-2 class")

obj = B()
obj = C()
obj.display()
obj.displayB()
obj.displayC()