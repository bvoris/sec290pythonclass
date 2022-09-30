#
# SEC290.12780.B1.Online
# Brad Voris
# 9/25/2022
# Week 4 Programming Assignmnet
#

window_attributes =""
menu = """

     Window Administration Application

     a: Exit application
     b: Enter an attribute
     c: Calculate and display the aspect ratio
     d: Display the window attributes and values
     
"""
print(menu)
input()
done = False
while not done:
    print(menu)
    selection = input("Please make a selection: ")
    print()
    if selection == "a":
        done == True
        break
    elif selection == "b":
        print("Enter an attribute: ")       
        print()
        input("Press Enter to return to the menu...")
    elif selection == "c":
        print("Calculate and display the aspect ratio: ")
        print()
        input("Press Enter to return to the menu...")
    elif selection == "d":
        print("Display the window attributes and values: ")
        print()
        input("Press Enter to return to the menu...")
    else:
        print("Please select a, b, c, or d")


print("Exiting the application...")
input()
