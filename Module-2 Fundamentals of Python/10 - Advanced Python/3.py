"""
Write a Python program that filters out even numbers using the filter() function.
"""

l1 = [12,3,67,88,45,22]

l2 = list(filter(lambda n : n % 2 == 0,l1))

print(l2)