#Create a python program to create a text file which includes
# User name (input)
# Age  (input)
# Date of Birth (input)
# Delivery :: Github link files.py

user_name = input("Enter your name: ")
age = input("Enter your age: ")
date_of_birth = input("Enter your date of birthday (DD-MM-YYYY): ")

with open("user_Info.txt", "a") as file:
    file.write("User Name: " + user_name + "\n")
    file.write("Age: " + age + "\n")
    file.write("Date of Birth: " + date_of_birth + "\n")


