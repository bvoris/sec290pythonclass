#
# SEC290.12780.B1.Online
# Brad Voris
# 10/05/2022
# week 6 Step 2
import time

menu = """

Forum Comments
==============
0: Exit
1: Display Comments
2: Add Comment

"""
dictionary=[]
selection =6
file = "step2_data.txt"

try:
    dictFile = open(file,'r')
except FileNotFoundError:
    print("The file is not found...")
    quit()
else:
    dictFile.readline()
    for lines in dictFile:
        temp = lines.split("\t")
        # print(temp)
        lineDict = {"date":temp[0],"name":temp[1],"comment":temp[2]}
        dictionary.append(lineDict)
   
while(selection!=0):
    print(menu)
    selection = int(input())
    if(selection==0):
        print("\nThank you for Participation...")
    elif(selection==1):
        for dict in dictionary:
            print("\n",dict["name"],"   ",dict["date"])
            print("\n", dict["comment"])
            print("\n-----------------------------")

    elif(selection==2):
        currentTime = time.ctime()
        userName = input("Enter Your Name: ")
        comment = input("Enter the comment: ")
        tempDict = {"date":currentTime,"name":userName,"comment":comment}
        dictionary.append(tempDict)
    else:
        print("Wrong Selection, please enter 0, 1, or 2")

