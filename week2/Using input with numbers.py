#Using input() with numbers
item_1= input("Please enter the price of the first item: ")
item_2= input("Please enter the price of the second item: ")
item_3= input("Please enter the price of the third item: ")
total = item_1 + item_2 + item_3
print("Your total cost is: " total)
#Input alwaays returns a string Program above fails
#Using input() with numbers
item_1= input("Please enter the price of the first item: ")
item_2= input("Please enter the price of the second item: ")
item_3= input("Please enter the price of the third item: ")
item_1= float(item_1)
item_2= float(item_2)
item_3= float(item_3)
total = item_1 + item_2 + item_3
print("Your total cost is: " total)
#converting string to an integer
a = "525"
b = "25"
c = 35
a + b # concatinates a and b as 52525
a + c # Fails because a is a string and b is an integer
a = int(a)
b = int(b)

#Converting integers to strings
price = 5.35
price = str(price)

#format specifiers for floating point numbers (decimal places)
val = 8/3
print(val) #displays as 2.666666666666665
print(f'${val:6.2f}') #displays as $ 2.67
print(f'${val:06.2f}')#displays as $002.67
print(f'${val:2f}')#displays as $2.67
