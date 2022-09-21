#Week 4 4.0 Secure programming
# input validation
# exception handling
#no input validatation bad data type data doesn't match type within a valid range

#attackers look for ways to compromise a system bvy entering data that causes the program to crash or enable unauthorized access

#no input validate data out of range (menu system with options 1, 2, 3 and someone inputs 8)
#input validation through loops

#Handling exceptions
#programs shouldn't crash
#exceptions can be causght and handled using try/except
#try except can enable an applicaiton to recover from an exception or exit gracefully

#try/except is another tool for input validation
score = input("Please enter your score: ")
try:
    score = float(score)
except ValueError:
    print("Invalid input.")
    print("{} is not a number.".format(score))
else:
    print("You're Awesome!")
print("Done!")

# Crashing -"Throwing an exception"