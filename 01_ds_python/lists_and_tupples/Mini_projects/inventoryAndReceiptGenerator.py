
"""
Project 1: Inventory & Receipt Generator
This project combines list iteration, tuple unpacking, and formatted string output.

Scenario: You represent products in a store using a list of tuples, where each tuple is (item_name, price, quantity_sold).

Python
cart = [
    ("Laptop", 999.99, 1),
    ("Wireless Mouse", 25.50, 2),
    ("HDMI Cable", 12.00, 3),
    ("USB-C Hub", 45.00, 1)
]
Requirements:

Iterate over the cart list. In your for loop header, unpack (item, price, qty) directly.

Compute item total (price * qty) for each row.

Print a formatted receipt line for each item (e.g., Wireless Mouse x2 = $51.00).

Track the grand total and total items sold, then return them packed as a tuple (total_items, grand_total) at the end."""


cart = [
    ("Laptop", 999.99, 1),
    ("Wireless Mouse", 25.50, 2),
    ("HDMI Cable", 12.00, 3),
    ("USB-C Hub", 45.00, 1)
]

def inventorFunction():
    totalSum = 0
    count = 0
    for (item, price, qty) in cart:
        total = price * qty
        print(f"{item} x{qty} = {total}")
        totalSum += total
        count += qty

    return (count, totalSum)
        

def main():
    qty, grandTotal = inventorFunction()
    print(f"Total Items Sold: {qty}, Grand Total :{grandTotal}")

main()
    