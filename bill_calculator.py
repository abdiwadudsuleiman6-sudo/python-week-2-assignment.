# Step 1: Ask the user for inputs and convert data types
price = float(input("Enter the price of one item: "))
quantity = int(input("Enter the quantity you want: "))

# Step 2: Calculate the total bill
total = price * quantity

# Step 3: Print a friendly summary using an f-string
# The :.2f ensures the numbers display beautifully like money (e.g., 50.00)
print(f"{quantity} items at {price:.2f} each = {total:.2f}")
