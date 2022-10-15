#
# SEC290.12780.B1.Online
# Brad Voris
# 10/05/2022
# week 6 Exercise 6-4

import json
fname = "ex6-4.json"
try:
    fp = open(fname)
except:
    numbers = []
else:
    ds = json.load(fp)
    numbers = ds["numbers"]
    fp.close
print(f'Number: {numbers}')
while True:
    num = input("Please enter a number (or use the enter key to exit):")
    if len(num) <=0:
        break
    else:
        num = int(num)
        numbers.append(num)
ds = {"numbers": numbers}
fp = open(fname, "w")
json.dump(ds, fp)
fp.close
