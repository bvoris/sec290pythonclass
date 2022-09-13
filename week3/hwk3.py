#
# SEC290.12780.B1.Online
# Brad Voris
# 9/16/2022
# Week 3 Programming Assignmnet
#

from random import randint
randomnumber = randint(1,20)
num_lives = 3

print("Welcome to the Secret Number Guessing Game!")
print()
print("Rules: You have 3 tries to get the secret number, which is a random number between 1 and 20")
print()

while num_lives > 0:
    print(f'Lives Remaining: {num_lives}')
    guess = int(input("Guess the secret number: "))
    print()
    num_lives = num_lives - 1
    if guess == randomnumber:
        print(f'you guessed {guess} and the random number matched {randomnumber}')
        print("Congratulations on guessing the correct numer!")
        print()
        break
    elif guess > randomnumber:
        print(f'You guessed {guess} and the random number was smaller, try again... ')
        print()
    elif guess < randomnumber:
        print(f'You guessed {guess} and the random number was larger, try again... ')
        print()        
    else:
        Done
        
    if num_lives == 0:
        print(f'The random number was {randomnumber}')
        print("Better luck next time!")
        break
print()
print("Done!")
input()

