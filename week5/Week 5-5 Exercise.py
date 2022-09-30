#
# SEC290.12780.B1.Online
# Brad Voris
# 9/28/2022
# week 5 Exercise 5-5

greeting_list = []
names_list  = []
print("Construct a greeting one letter at a time.")
print("When done press the enter key... ")
while True:
    letter = input("please enter a letter: ")
    if len(letter) == 0:
        break
    greeting_list.append(letter)
print()
print("Construct a list of names to be greeted.")
print("When done press the enter key...")
while True:
    name = input("please enter a name: ")
    if len(name) == 0:
        break
    names_list.append(name)
print()
greeting = "".join(greeting_list)
names = ",".join(names_list)
print(f'{greeting} to {names}!')