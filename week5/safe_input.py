#
# SEC290.12780.B1.Online
# Brad Voris
# 9/28/2022
# week 5 Exercise 5-2 safe input

def int_input(prompt):
    while True:
        str_num = input(prompt)
        try:
            num = int(str_num)
        except ValueError:
            print (f'"{str_num}" is not a numbner.')
            print ("Please try again, numbers only, please.")
        else:
            break
    return num