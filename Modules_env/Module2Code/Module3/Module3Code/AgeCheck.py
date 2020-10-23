'''
MSc Digital and Technology Solutions
CETM65 Software Engineering Principles
Author: Paul Jones
Student Number: bh83dq
Date: 23/10/2020
'''

# Module3 - AgeCheck.py

print("Verifying that Module: 'AgeCheck' has been successfully imported")   # prints a bit of code to show the module was successfully imported
print("VERIFIED")                                                           # prints a bit of code to show the module was successfully imported

def AgeCheck(Age):
    if Age.Age <=22:
        print("You are too young to access this information")
    else:
        print("Age acceptable - Access granted")