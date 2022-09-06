#Slice
#Slice is a copy of a subset of list tuple or string
birds = ("finch","cardinal","crow","wren")
print("Tuple of birds:", birds)

middle_two = birds[1:3]
print("Slice of the middle two elements:", middle_two)

first_two = birds[: 3]
print("slice of the first two elements", first_two)

last_two = birds[2 :]
print("slice of the last two elements:", last_two)

complete_copy = birds[ : ]
print("Here's a copy of the tuple:", complete_copy)

#shorthand trick for slice
birds_copy = birds[0:len(birds)]
print(birds_copy)
