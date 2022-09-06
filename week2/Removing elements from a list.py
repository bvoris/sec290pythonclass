#using pop() to remove elements from a list
birds = ["finch", "cardinal", "crow", "wren"]
print("Original list:", birds)

last_element = birds.pop()
print(f'The last element - {last_element} - has been removed from')

second_element = birds.pop(1)
print(f'The second element - {second_element} - has been removed from the list.')

print("Modified List", birds)

birds = ["finch", "cardinal", "crow", "cardinal", "wren"]
print("Original List:", birds)
birds.remove("cardinal")
print("List with the first occurance of 'cardinal' removed:\n", birds)

birds = ["finch", "cardinal", "crow", "wren"]
print("Original list:", birds)

birds.insert(2, "eagle")
print("List with 'eagle' added: ", birds)

#Sorting and reversing

birds.sort()
print("original list sorted:", birds)
birds.reverse()
print("original list reversed:", birds)