'''
MSc Digital and Technology Solutions
CETM65 Software Engineering Principles
Author: Paul Jones
Student Number: bh83dq
Date: 23/10/2020
'''

# Module2 - ID.py

print("Verifying that Module: 'ID' has been successfully imported") # prints a bit of code to show the module was successfully imported
print("VERIFIED")                                                   # prints a bit of code to show the module was successfully imported


class Person(): #Defines a class in python, in this case the class is called 'River'

    def __init__(self, Forename, Surname, Title, Age): # This initialises the class to have initial values of RiverName and Location
        self.Forename = Forename #sets the attributes for each instance of the class
        self.Surname = Surname #sets the attributes for each instance of the class
        self.Title = Title #sets the attributes for each instance of the class
        self.Age = Age #sets the attributes for each instance of the class
    
    def __str__(self):
        return f"Name: {self.Surname}, {self.Forename}. Title: {self.Title}. Age: {self.Age}"

    def __repr__(self):
        return "Person()"