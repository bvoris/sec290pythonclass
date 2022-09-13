#
# SEC290.12780.B1.Online
# Brad Voris
# 9/13/2022
# Week 3 Exercise Set
#

# Exercise 1
print("Welcome to the Association Football Survey")
print()
userrating = int(input("Please rate your interest in Association Football on a scale of 1 to 3 with 1 being great and 3 being terrible. "))
if userrating == 1:
    print("I love it, too!")
elif userrating == 2:
    print("I could take it or leave it as well.")
elif userrating == 3:
    print("Not my cup of tea, either.")
else:
    print("Please answer the question with 1, 2 or 3!")
print()
input()
print("Push enter to move on to Exercise 2")
print()
input()

# Exercise 2
from random import randint
total = 0
num_additions = 0
while total <= 1000:
    num = randint(1,10)
    total = total + num
    additions = num_additions + 1
    num_additions += 1 # I kept having problems here, this would only = 1
    print(f'Total: {total}, # of additions: {num_additions}')
print("Done!")
print()
input()
print("Push enter to move on to Exercise 3")
input()

# Exercise 3
listedvalues = [8, 10, 200, 10, 30, 40, 10]
print(f'My list values are: {listedvalues}')
while 10 in listedvalues:
    listedvalues.remove(10)
    print(f'Removed 10. Remaining listed values: {listedvalues}')
print("Done!")