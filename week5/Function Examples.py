from morse import alpha_to_morse
letterlist = []
def test(case):
    #case = uppercaseword
    transval = []
    print(case)
    letterlist = list(case)
    print(letterlist)
    for i in letterlist:
        transval = alpha_to_morse[i]    
        print(transval, end=" ") #This prints out fine.
    #jointhem = ' '.join(transval)
        #joinedtransval = ','.join(transval)
        #print(joinedtransval)
    return  " ".join(transval)

uppercaseword = input("Write and uppercase word: ")

print(f'What was your word?: ',test(uppercaseword))