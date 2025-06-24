# Write a Python program to show method overloading.

class Calculator:
    def add(self,a,b):
        return a+b
calc = Calculator()
print(calc.add(5,10))
print(calc.add(25,30))