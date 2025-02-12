# Import Module
import random
from pprint import pprint

# Menu Options
menu_options = {"Deposit": "D", "Withdraw": "W", "Quit": "Q"}

# Generate a random initial balance
initial_balance = random.randint(-1000, 10000)

# Selection Menu
width = 40
fill_char = '*'
title = "PIXELL RIVER FINANCIAL"
sub_title = "ATM Simulator"

print(fill_char * width)
print(title.center(width))
print(sub_title.center(width))
print()
print(f"Your current balance is: ${initial_balance:.2f}".center(width))
print()
for key, value in menu_options.items():
    print(f"{key}: {value}".center(width))
print(fill_char * width)