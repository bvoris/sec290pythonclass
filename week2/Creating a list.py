#Creating the list and the for loop
#list is a data structure similar to an array
#list variable has more than one value at the same time like a row in excel
#members of a list are called elements
#each element of a list can be accessed using an index
#list data structure includes several methods for manipulating a list
#lists can contain strings, integers, flkoats, objects, and other data structures

#some_list = []
birds = ["crow","finch","cardinal","wren"]
print(birds)
print(birds[0])
print("Initial list:", birds)
birds.append("eagle")
print("Modified list:", birds)

#indexing and access to elements in a list
print("First element: ", birds[0])
print("Last element: ", birds[len(birds)-1])
print("Last element using -1 as an index", birds[-1])
