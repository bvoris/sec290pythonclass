#
# SEC290.12780.B1.Online
# Brad Voris
# 9/25/2022
# Week 4 Programming Assignmnet
# Step 1

menu = """
a: Exit the application
b: Enter an attribute
c: Calculate and display the aspect ratio
d: Display the window attributes and values

"""
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
        input()
    elif selection == "c":
        print("Calculate and display the aspect ratio: ")
        print()
        input()
    elif selection == "d":
        print("Display the window attributes and values: ")
        print()
        input()
    else:
        print("Please enter a, b, c, d")
        print()
        input()
print("Done!")
        