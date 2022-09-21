#Modules
#the random module for random values
import random
val = random.randint(1,10)
print(f"Here's a random value: {val}")

#using aliases with modules
import random 
val = random.randint(1,10)
print(f"Here's a random value: {val}")

#shuffle function
import random as r
players = ['Helena','Marina','Matthew','Max','Yelba']
print(f'original: {players}')
r.shuffle(players)
print(f'shuffled {players}')

