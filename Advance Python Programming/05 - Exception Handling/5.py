# Write a Python program to handle file exceptions and use the finally block for closing the file.
try:
    with open("myfile3.txt","r") as file:
         print(file.read())

except FileNotFoundError:
     print("File does not exist!")

except Exception as e:
     print("An unexpected error : {e}")

finally:
    try:
          file.close()
          print("File closed succcessfully")
    except:
         print("File was not open")