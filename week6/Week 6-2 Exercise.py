#
# SEC290.12780.B1.Online
# Brad Voris
# 10/05/2022
# week 6 Exercise 6-2

fp = open("ex6-2-data.txt")
line_number = 1
for line in fp:
    line = line.strip()
    print(f'{line_number}#: {line}')
    line_number += 1
    
fp.close