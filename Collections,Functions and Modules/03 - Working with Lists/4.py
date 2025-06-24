# Write a Python program to insert elements into an empty list using a for loop and append().

list = []
n = int(input("Enter number of elements you want to enter : "))

for i in range(n):
    element = input("Enter elements : ")
    list.append(element)
print(list) 