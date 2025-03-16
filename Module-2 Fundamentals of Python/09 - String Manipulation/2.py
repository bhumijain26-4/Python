"""
Write a Python program that manipulates and prints strings using various string methods.
"""
str = "Python Programming | java Programming"

print(len(str))
print(str.lower())
print(str.upper())
print(str.capitalize())
print(str.title())
print(str.strip())
print(str.replace("python","java"))
print(str.find("python"))
print(str.startswith("python"))
print(str.endswith("java"))

str2 = print(str.split())

print(str.isalpha())
print(str.isdigit())
print(str.isalnum())
print(str.zfill(42))