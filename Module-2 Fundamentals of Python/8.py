"""
Write a Python program to test whether a passed letter is a vowel or not.
"""
char = input("Enter any character: ")
if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u' or char == 'A' or char == 'E' or char == 'I' or char == 'O' or char == 'U' :
    print("Vowel",end="")
else:
    print("Consonant",end="")