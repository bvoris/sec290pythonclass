import time,json
from turtle import heading
from unicodedata import name
record_list=[]
choice =6
file = "step3.txt"
try:
    recordFile = open(file,'r')
except FileNotFoundError:
    print("The file is not found")
    pass
else:
    recordFile.readline()
    for lines in recordFile:
        temp = lines.split("\t")
        # print(temp)
        lineDict = {"date":temp[0],"name":temp[1],"comment":temp[2]}
        record_list.append(lineDict)
    

while(choice!=0):
    print("Forum Comments")
    print("\n===============")
    print("\n0:Exit")
    print("\n1.Display Comments")
    print("\n2.Add Comment")
    choice = int(input())
    if(choice==0):
        print("\nThankyou for Participation")
    elif(choice==1):
        for record in record_list:
            print("\n",record["name"],"   ",record["date"])
            print("\n", record["comment"])
            print("\n-----------------------------")

    elif(choice==2):
        currentTime = time.ctime()
        userName = input("Enter Your Name")
        comment = input("Enter the comment")
        tempDict = {"date":currentTime,"name":userName,"comment":comment}
        record_list.append(tempDict)
    else:
        print("Wrong Selection")
newRecordsFile = open(file,'w')
heading = "Date\tName\tComment\n"
newRecordsFile.write(heading)
for record in record_list:
    line = str(record["date"]) + "\t"+record["name"]+"\t"+record["comment"]+"\n"
    newRecordsFile.write(line)
