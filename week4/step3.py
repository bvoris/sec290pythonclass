#
# SEC290.12780.B1.Online
# Brad Voris
# 9/25/2022
# Week 4 Programming Assignmnet
# Step 3

menu = """
a: Exit the application
b: Enter an attribute
c: Calculate and display the aspect ratio
d: Display the window attributes and values
e: Clear the dictionary
"""
# I added e so that I could clear the attributes and start over.

# Empty dictionary created
dictionary = {}
# Variables containing width and height for comparison
widthcomparevar = 'width'
heightcomparevar = 'height'

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
        print()
        attributevalue = input("Please enter the attribute value: ")
        print()
        print(f'The attribute name is {attributename} and the attribute value is {attributevalue}')
        dictionary[attributename] = attributevalue
        print()
        print(f'{attributename}:{attributevalue} have been added to the dictionary.')
        input()
    elif selection == "c":
        print("Calculate and display the aspect ratio: ")
        if widthcomparevar in dictionary:
            print(f'Yes, {widthcomparevar} exists in the dictionary. ')
            if heightcomparevar in dictionary:
                print(f'Yes, {heightcomparevar} exists in the dictionary.')
                print()
                print("all is good for the keys in the dictionary to proceed...")
                input()
                # Integer conversion for width/height
                try:
                    numericwidthvar = int(dictionary['width'])
                except ValueError:
                    print("Invalid input.")
                    print("{} is not a number.".format(numericwidthvar))
                else:
                    try:
                        numericheightvar = int(dictionary['height'])
                    except ValueError:
                        print("Invalid input.")
                        print("{} is not a number.".format(numericheightvar))
                    else:   
                        print()
                        print("all is good for the values in the dictionary to proceed...")
                        input()
                        # print converted value types
                        print("Width value has been converted to: ")
                        print(type(numericwidthvar))
                        print()
                        print("Width value has been converted to: ")
                        print(type(numericheightvar))
                        print()
                        # Aspect Ration Calculator
                        if numericheightvar <= 1:
                            print("Invalid input.")
                            print("Height cannot be 0. Please set height as 1 or greater.")
                        else:
                            aspectratio=round(float(numericwidthvar/numericheightvar),2)
                            print(f'The aspect ratio is {aspectratio}')                
                        
            else:
                print(f'No, {heightcomparevar}, is not in the dictionary, please enter selection "b: Enter an attribute"')
        else:
            print(f'No, {widthcomparevar}, is not in the dictionary, please enter selection "b: Enter an attribute"')
        print()        
        input()
    elif selection == "d":
        print("Display the window attributes and values: ")
        for key, value in dictionary.items():
            print("{} : {}".format(key,value))
            print()
        input()
    elif selection == 'e':
        print("clearing all items from the dictionary...")
        dictionary.clear()
        input()
    else:
        print("Please enter a, b, c, d, e")
        print()
        input()
print("Done!")
        