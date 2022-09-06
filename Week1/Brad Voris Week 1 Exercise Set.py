# Class Work by: Brad Voris
# Exercise 1 Week 1

# Simple Printing
# Part 1 Variables
animal = "monkey"
vegetable = "onion"
mineral = "diamond"

print(animal, vegetable, mineral)

# Part 2 Output formatting
# I don't follow sports so I am picking a band.
team = "Crowbar"
status = "touring"
punctuation = "."

print (team, status, punctuation)
# Additional testing with punctuation
print(f"The band {team} is {status} in North America{punctuation}")

# Part 3 Getting user input
date = input("Enter the date:")
print ("Oh, I am sorry. I am not available on " + date +".")

# Part 4 Triple Quoted Strings
wilmu_classes = """
SEC250
SEC350
SEC425
"""
# Print triple quote variable
print(wilmu_classes)
# Print as formated text
print(f"\nSEC250\nSEC350\nSEC425")