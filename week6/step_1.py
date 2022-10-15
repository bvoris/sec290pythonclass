#
# SEC290.12780.B1.Online
# Brad Voris
# 10/05/2022
# week 6 Step 1
import time

menu = """

Forum Comments
==============
0: Exit
1: Display Comments
2: Add Comment

"""
dictionary = {}

while True:
    print(menu)    
    selection = input("Please make a selection: ")
    if selection == "0":        
        print(f'Your selection was: {selection}')        
        break
    elif selection == "1":        
        print(f'Your selection was: {selection}')
        print()
        for i in dictionary:
            print("Date: ",dictionary["date"],"Username: ",dictionary["name"])
            print("Comment: ", dictionary["comment"])
            print("\n-----------------------------")
        input()
    elif selection == "2":        
        print(f'Your selection was: {selection}')
        date = time.ctime()
        name = input("What is your name? ")
        comment = input("What is your comment? ")
        dictionary = {"date":date,"name":name,"comment":comment}
        
    else:
        print("Invalid selection, please choose 0, 1, or 2")
        input()

print("Thank you for your participation! Now exiting...")
        
        