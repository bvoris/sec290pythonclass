#
# SEC290.12780.B1.Online
# Brad Voris
# 9/28/2022
# week 5 Exercise 5-4

number_str = "28 81 27 4"
total = int(0)
numbers = number_str.split(" ")

for num in numbers:
    num = int(num)
    total += num
print(f'The total is {total}.')
