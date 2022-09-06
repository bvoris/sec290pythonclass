#
# SEC290.12780.B1.Online
# Brad Voris
# 9/6/2022
# HWK #2 
#

title_var = """
    Welcome
    to the
   Party Pal!
"""
print(title_var)

# List of party attendees
listofnames = ["Alexa Araujo", "Andrew Barnhart", "Wendy Boucher", "Gregory Clanton", "James Cryderman", "Mavrick Foster", "Andrew Gyimah", "Nathaniel Humphrey", "Stephen Johnson", "Samantha Legg"]

# Sorted list of party attendees
namelist = sorted(listofnames)

# Sorted, numbered, printed list of party attendees
print()
print("The party attendees are: ")
for i, name in enumerate(namelist):
    print(f'Party Attendee {i+1}: {name}')
print()

# Attendee Change request    
print()
print("Oops! It turns out one of your guests can't make it.")
print()
cancelrequest = input("Which guest do you want to change? ")
cancelrequest =(int(cancelrequest)-1)
print()
print(f'The following will not be attending:', namelist[cancelrequest])
print()

# Remove the canceled party attendee
namelist.pop(cancelrequest)

# Display updated changes
print("The updated party attendees are: ")
print()
for i, name in enumerate(namelist):
    print(f'Party Attendee {i+1}: {name}')
print()

# Adding another attendee and confirm
newattendee = input("Who is the new attendee to the party? ")
namelist.append(newattendee)
print()
print(f'The following attendee has been added to the list:', newattendee)
print()

# Sort the name list
namelist = sorted(namelist)

# Display updated changes
print()
print("The updated party attendees are: ")
print()
for i, name in enumerate(namelist):
    print(f'Party Attendee {i+1}: {name}')