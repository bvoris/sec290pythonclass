# Importing Modules
from tips import tip_calculator

bill = input("How much was the bill? ")
try:
    bill =float(bill)
except ValueError:
    print("Please enter an amount as a number. ")
else:
    tip, total = tip_calculator(bill, "low")
    print(f'Price: {bill:6.2f}, Tip: {tip:6.2f}, Total: {total:6.2f}')
    tip, total = tip_calculator(bill, "average")
    print(f'Price: {bill:6.2f}, Tip: {tip:6.2f}, Total: {total:6.2f}')
    tip, total = tip_calculator(bill, "high")
    print(f'Price: {bill:6.2f}, Tip: {tip:6.2f}, Total: {total:6.2f}')