#week 3 3.6
#Counting in a while loop
count = 0
done = 0
while done == 0:
    count = count + 1
    print("Loop count: {}".format(count))
    value = input("please enter a value: ")
    if value[0] == "q":
        done = 1
        
print("Done! ")