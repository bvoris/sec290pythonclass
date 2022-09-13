#best use of a while loop
import random
done = False # initial condition
#
# keep running the loop until you get a 5
# from randint
#
while not done:
    # Get a random value between 1 and 10
    value = random.randint(1,10)
    print("Random Value: {}".format(value))
    if value == 5:
        done = True # Change the loop variable
                    # to exit
print("Done!")