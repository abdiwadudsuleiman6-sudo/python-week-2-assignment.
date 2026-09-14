# Python Week 2 Assignment - Bill Calculator

This is a simple interactive terminal calculator that prompts the user for an item's price and quantity, then computes and prints a formatted receipt summary.

### Python Source Code
\`\`\`python
# Step 1: Ask the user for inputs and convert data types
price = float(input("Enter the price of one item: "))
quantity = int(input("Enter the quantity you want: "))

# Step 2: Calculate the total bill
total = price * quantity

# Step 3: Print a friendly summary using an f-string
print(f"{quantity} items at {price:.2f} each = {total:.2f}")
\`\`\`
