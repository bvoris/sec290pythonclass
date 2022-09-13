#The break statement
guests = []
while True:
    guest = input("Please enter a guest to be invited: ")
    if guest == "exit":
        break
    guests.append(guest)
print("Guest list is complete!")
print(f'Guest list: {guests}')