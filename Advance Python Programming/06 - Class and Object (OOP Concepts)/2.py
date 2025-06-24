# 12) Write a Python program to demonstrate the use of local and global variables in a class.

#local variable
def myfun():
       name="Python Language"  # it is declared inside the function
       print(name)  
name="Python"

myfun()


#global variable
def myfun():
       print(name)

name="Python"        # it is declared outside the function

myfun()