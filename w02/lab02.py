# 1. Name: 
#    Celeste George
# 2. Assignment Name: 
#    Lab 02: Authentication
# 3. Assignment Description:
#    Write a program to read the contents of the file into a list.
#    The program will then prompt the user for a username and password.
#    Lastly, we will tell the user whether the user is authenticated.
# 4. What was the hardest part? Be as specific as possible.
#    The hardest part was actually trying to load in my json file into my
#    program. I kept running into the same error of not being able to 
#    locate the file on my comptuer. After researching some tips, I decided
#    to put the direct path of the json file on my computer with double
#    backward slashes. Once I solved this bug everything else fell into place.
# 5. How long did it take for you to complete the assignment?
#    2.5 hours

import json

# open the JSON file -> Used backslahes and path to indicate to the program
#   where the json file is located since I kept running into errors. By addding
#   the path location on my computer now the program runs.
fileName = "C:\\Users\\celes\\Desktop\\cse130\\w02\\Lab02.json"
try:
    with open(fileName, "r") as myfile:
        data = json.load(myfile)

# 2 seperate error codes for json file -> I had to add more specific error codes
#   in order to find out why my json file was not opening.
except FileNotFoundError:
    print(f"File {fileName} not found.")
    exit(1)
except json.JSONDecodeError:
    print(f"Invalid JSON in {fileName}.")
    exit(1)

# create lists from JSON data
passwords = data.get("password", [])
usernames = data.get("username", [])

# prompt for username and password -> Used secret so I would not lose the variable
#   name since passwords has already been used multiple times in program.
user = input("Username: ")
secret = input("Password: ")

# check if user input is authenticated
if user in usernames and secret == passwords[usernames.index(user)]:
    print("You are authenticated!")
else:
    print("You are not authorized to use the system.")