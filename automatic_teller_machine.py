# Import Module
import random
from pprint import pprint
import time
import os

# Menu Options
menu_options = {"Deposit": "D", "Withdraw": "W", "Quit": "Q"}

# Generate a random initial balance
initial_balance = random.randint(-1000, 10000)

# Selection Menu
width = 40
fill_char = '*'
header_footer = fill_char * width
title = "PIXELL RIVER FINANCIAL"
sub_title = "ATM Simulator"
trigger_menu = True
# Selection Menu Loop
while (trigger_menu):
    print(header_footer)
    print(title.center(width))
    print(sub_title.center(width))
    print()
    print(f"Your current balance is: ${initial_balance:.2f}".center(width))
    print()
    for key, value in menu_options.items():
        print(f"{key}: {value}".center(width))
    print(header_footer)
    selection = input(f"Enter your selection: ")
# Deposit, Withdraw, Quit Loop
    if selection in ['d', 'D']:
        amount = float(input(f"Enter the transaction amount: "))
        current_balance = initial_balance + amount
        print()
        print(header_footer)
        print(f"Your current balance is: ${current_balance:.2f}".center(width))
        print(header_footer)
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')
    elif selection in ['w', 'W']:
        amount = float(input(f"Enter the transaction amount: "))
        current_balance = initial_balance - amount
        if amount >= current_balance:
            print()
            print(header_footer)
            print(f"INSUFFICIENT FUNDS".center(width))
            print(header_footer)
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
        elif amount < current_balance:
            print()
            print(header_footer)
            print(f"Your current balance is: ${current_balance:.2f}".center(width))
            print(header_footer)
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
    elif selection in ['q', 'Q']:
        break
    else:
        print()
        print(header_footer)
        print(f"INVALID SELECTION".center(width))
        print(header_footer)
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')