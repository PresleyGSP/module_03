# Import Module
from pprint import pprint
from csv import DictReader

# File I/0
data = {}

with open("account_balances.txt", "r") as input_file:
    for line in input_file:
        key, value = line.strip().split('|')
        data[key] = float(value)
    pprint(data)
for key, value in data.items():
    if value < 0:
        interest_rate = 0.1
    elif value < 1000:
        interest_rate = 0.01
    elif value < 5000:
        interest_rate = 0.025
    else:
        interest_rate = 0.05
    monthly_interest = value * interest_rate / 12
    new_value = value + monthly_interest
    data[key] = new_value
for key, value in data.items():
    pprint(f"{key}: {value:.6f}")

with open("updated_balances_PMG.csv", "a") as file:
     file.write(f"Account,Balance")
     for key, value in data.items():
        file.write(f"\n{key},{value:.2f}")
    