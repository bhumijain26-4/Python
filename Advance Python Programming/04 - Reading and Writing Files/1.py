# Write a Python program to read the contents of a file and print them on the console.

with open("myfile.txt","r") as file:
    contents = file.read()

print(contents)