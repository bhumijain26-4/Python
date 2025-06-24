# Write a Python program to read a file and print the data on the console. 

with open("file.txt","r") as file:
    contents = file.read()

print(contents)
