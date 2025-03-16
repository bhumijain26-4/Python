"""
Write a Python program to apply the map() function to square a list of numbers.
"""

l1 = [5,11,15,20,25]

l2 = list(map(lambda n : n * n , l1))

print(l2)