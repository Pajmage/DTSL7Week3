'''
MSc Digital and Technology Solutions
CETM65 Software Engineering Principles
Author: Paul Jones
Student Number: bh83dq
Date: 23/10/2020
'''

import Module2Code.ID as ID # This code will import the ID module from the Module2Code folder and will name it ID using the as keyword
                            # This means that I can simply use 'ID' to refer to the imported module rather than needing the full filepath.

import Module2Code.Module3.Module3Code.AgeCheck as Age # again, this code is importing a new module using a keyword to avoid needed to constantly type out the full file path when referring to functions etc from said module

Bob = ID.Person("Smith", "Bob", "Dr", 23)           # Creates an instance of the Person class imported from the ID Module with the identifier of Bob
Lisa = ID.Person("Doe", "Lisa", "Ms", 18)           # Creates an instance of the Person class imported from the ID Module with the identifier of Lisa
John = ID.Person("Doe", "John", "Mr", 46)           # Creates an instance of the Person class imported from the ID Module with the identifier of John
Alice = ID.Person("Brown", "Alice", "Mrs", 21)      # Creates an instance of the Person class imported from the ID Module with the identifier of Alice

print(Bob)          # Print the contents of the Bob instance 
Age.AgeCheck(Bob)   # Run the AgeCheck function from the Module keyworded as Age passing in the information from the Person class instantiated from the ID module
print()
print(Lisa)         # Print the contents of the Lisa instance
Age.AgeCheck(Lisa)  # Run the AgeCheck function from the Module keyworded as Age passing in the information from the Person class instantiated from the ID module
print()
print(John)         # Print the contents of the John instance
Age.AgeCheck(John)  # Run the AgeCheck function from the Module keyworded as Age passing in the information from the Person class instantiated from the ID module
print()
print(Alice)        # Print the contents of the Alice instance
Age.AgeCheck(Alice) # Run the AgeCheck function from the Module keyworded as Age passing in the information from the Person class instantiated from the ID module
print()
