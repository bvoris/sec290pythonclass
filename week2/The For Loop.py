#The for loop
list_of_names = ["Jose", "Naomi", "Mike", "Claire"]
for name in list_of_names:
    print(name)
print("Done!")

#using enumerate() with a for loop
for i, name in enumerate(list_of_names):
    print(f' {i+1}: {name}')
print("Done!")