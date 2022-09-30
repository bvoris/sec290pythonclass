#
# SEC290.12780.B1.Online
# Brad Voris
# 9/28/2022
# week 5 Programming Assignment Step 2

# import modules
from morse import alpha_to_morse, morse_to_alpha

# Functions for step 2
def translate_to_morse(case):
    case = uppercaseword
    transval = alpha_to_morse[case]
    return transval
    
def translate_to_alpha(code):
    code = morsecode
    transval = morse_to_alpha[morsecode]
    return transval


# menu variable
menu = """

    Morse Code Translator
    
    0: Exit
    1: Translate a word into Morse Code
    2: Translate Morse Code to text.

"""
# Program body
while True:
    print(menu)    
    selection = input("Please make a selection: ")
    if selection == "0":        
        print(f'Your selection was: {selection}')        
        break
    elif selection == "1":        
        print(f'Your selection was: {selection}')
        word = input("Please input a letter to be converted: ")
# Value check for input validation is alpha (this took a bit of research and trial and error)
        wordvaluechecker = word.isalpha()
        if wordvaluechecker == True:
            try:
                uppercaseword = word.upper()
            except ValueError:
                print("Please input only a letter...")
            else:
                print()
                print(f'Your selection was {uppercaseword}, the Morse value is ',translate_to_morse(uppercaseword))
                input()
        else:
            print("Please input only a letter...")
            input()
    elif selection == "2":        
        print(f'Your selection was: {selection}')
        print("Below is the Morse Code to Alpha Dictionary: ")
# This wasn't required but its easier to visually see what the morse code is to select a letter
        print((str(morse_to_alpha)[1:-1]).replace("'",""))
        morsecode = input("Please input the morse code character to be converted to a letter: ")
# Input validation in this is pretty difficult        
        try:
            convertedvariable = morse_to_alpha[morsecode]                         
        except ValueError:
            print("Please input the correct code...")
        else:
            print()
            print(f'Your selection was {morsecode}, the Morse value is ', translate_to_alpha(morsecode))
        input()
    else:
        print("Invalid selection, please choose 0, 1, or 2")

print("Done!")
        
        