# The continue statement
guests = []
count = 0 # invite five guests, no doubles
while count < 5:
    guest = input("Please enter a guest to be invited: ")
    if guest in guests:
        print(f'{guest} is already in the guest list.')
        continue
    guests.append(guest)
    print(f"Guests: {guests}")
    count += 1 #same as count = count + 1
print("Guest list is complete! ")