#
# SEC290.12780.B1.Online
# Brad Voris
# 9/25/2022
# Week 4 Exercise
#

#Exercise 1
capitals = {}

while True:
    state = input("Please enter the name of the state: ")
    if state == 'q':
        break
    capital = input("Please enter the name of the capital: ")
    if capital == 'q':
        break
    capitals[state]=capital
print(f'States and their capitals: {capitals}')
input()

#Exercise 2
capitals = {"Delaware": "Dover", "New York": "Albany", "Florida": "Tallahassee"}

for state, capital in capitals.items():
    print(f"The capital of {state} is {capital}")
    print()
    
input()