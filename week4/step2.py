#
# SEC290.12780.B1.Online
# Brad Voris
# 9/25/2022
# Week 4 Programming Assignmnet
# Step 2

menu = """
a: Exit the application
b: Enter an attribute
c: Calculate and display the aspect ratio
d: Display the window attributes and values

"""
#Empty dictionary created
dictionary = {}

done = False
while not done:
    print(menu)
    selection= input("Please enter a selection: ")
    if selection == "a":
        done = True
        break
    elif selection == "b":
        print("Enter an attribute: ")
        print()
        attributename = input("Please enter the attribute name: ")
        attributevalue = input("Please enter the attribute value: ")
        print(f'The attribute name is {attributename} and the attribute value is {attributevalue}')
        dictionary[attributename] = attributevalue
        print(f'{attributename}:{attributevalue} have been added to the dictionary.')
        input()
    elif selection == "c":
        print("Calculate and display the aspect ratio: ")
        print()
        input()
    elif selection == "d":
        print("Display the window attributes and values: ")
        for key, value in dictionary.items():
            print("{} : {}".format(key,value))
            print()
        input()
    else:
        print("Please enter a, b, c, d")
        print()
        input()
print("Done!")
        