#
# SEC290.12780.B1.Online
# Brad Voris
# 9/28/2022
# week 5 Exercise 5-1

def int_input(prompt):
    while True:
        strtonum = input(prompt)
        try:
            number = int(strtonum)
        except ValueError:
            print(f'{strtonum} is not a number...')
            print("Please try again, numbers only.")
        else:
            break
    return number
number_1 = int_input("Please enter the first number to be added: ")
number_2 = int_input("Please enter the second number to be added: ")
total = number_1 + number_2
print(f'{number_1} + {number_2} = {total}')