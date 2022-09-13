# Menu based interface
menu = """
0: Exit
1: First Choice
2: Second Choice
"""

done = False
while not done:
    print(menu)
    selection = input("Please make a selection: ")
    print()
    if selection == "0":
        done == True
    elif selection == "1":
        print("First Choice")
    elif selection == "2":
        print("Second Choice")
    else:
        print("Please select 0, 1, or 2")
