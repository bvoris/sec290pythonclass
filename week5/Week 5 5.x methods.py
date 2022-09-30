# Week 5 Useful String Methods
# split()
# strip()
# join()
#
# split() method is used to plit a string into multiple fields based on a delimiting character
#
message = "the quick brown fox"
words = message.split(" ")
print(words)

line = "callaway,golf balls,2.99"
brand, item, price = line.split(",")
print(f'Brand: {brand}, Item: {item}, Price: ${price}')

# Strip() method
# strip method removes unwanted characters from the start and end of a string
# you can tell strip() what you want to have removed
message2 = "aaHello Word!aa"
print(message2)

fixedmessage = message2.strip("a")
print(fixedmessage)

message3 = "     uh-oh     "
print(f'My response is {message3}!')
message3_fixed = message3.strip()
print(f'My response is {message3_fixed}!')

# Join()
cities_list = ["Wilmington","Cairo","Orlando"]

cities_str = ",".join(cities_list)
print(f'And the cities are: {cities_str}')

letters = ["H","E","L","L","O"]
message4 = "".join(letters)
print(f'And the message is: {message4}')