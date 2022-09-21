# Dictionaries# Dictionaries are data structures that are modeled after a fphysical dictionary.
#sometimes referred to as an associative array, hash or hash table in other programming languages
# Dictionary traits key fetches a value
#in python dictionary
#a key must be unique and only appear once
# order is determined in which items are instered into a dictionary keys are not sorted
# an items key can be a string, number or any value that cannot change
# an items value can be anything even another dictinary

# Dictionary layout variable_name = {"key1":"value1", "key2":"value2"}
# adding or getting value use square brackets

capitals = {"Delaware":"Dover", "Colorado":"Denver", "Oregon":"Salem","Ohio":"Columbus"}
print(capitals)
print(capitals["Delaware"])
print(capitals["Ohio"])

#Assigning values to dictionaries
print("1: {}\n".format(capitals))
capitals["Maine"] = "Richmond"
print("2: {}\n".format(capitals))
capitals["Maine"] = "Agusta"
print("3: {}\n".format(capitals))

#Check if item exists in a loop
capitals = {"Delware":"Dover", "Colorado":"Denver", "Oregon":"Salem","Ohio":"Columbus"}
if "Delware" in capitals:
    print("Found it!")
else:
    print("Not Found!")
    
#Checking values to see if they are in the dictionary
capitals = {"Delware":"Dover", "Colorado":"Denver", "Oregon":"Salem","Ohio":"Columbus"}
vals = capitals.values #gets a list of values
if "Columbus" in vals():
    print("Found it!")
else:
    print("Not Found!")

#Finding keys
capitals = {"Delware":"Dover", "Colorado":"Denver", "Oregon":"Salem","Ohio":"Columbus"}
keys = capitals.keys()
for key in keys:
    print(key)

#Delete an item from a dictionary
capitals = {"Delware":"Dover", "Colorado":"Denver", "Oregon":"Salem","Ohio":"Columbus"}
print("1: {}\n".format(capitals))
del(capitals["Colorado"])
print("2: {}\n".format(capitals))

#using a dictionary in a for loop
capitals = {"Delware":"Dover", "Colorado":"Denver", "Oregon":"Salem","Ohio":"Columbus"}
for state in capitals:
    print("{} is the capital of {}".format(capitals[state],state))
print()
#Getting both the key and the value
capitals = {"Delware":"Dover", "Colorado":"Denver", "Oregon":"Salem","Ohio":"Columbus"}
for state, cap in capitals.items():
    print("{} is the capital of {}".format(cap,state))