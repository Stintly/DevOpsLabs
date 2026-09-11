inventory = 0

while True:
    user_input = input("Enter the number of items to add to inventory (or type 'exit' to quit): ")
    if user_input.lower() == 'exit':
        break

    if not user_input.isdigit():
        print("Please enter a valid number.")
        continue

    quantity = int(user_input)
    inventory += quantity

    if inventory > 500:
        print("Warning: Inventory exceeds maximum capacity of 500 items.")
        break
    elif inventory == 500:
        print("Inventory is at maximum capacity of 500 items.")

    else:
        print(f"Current inventory: {inventory} items.")


print("Final Report")
print(f"Total inventory recorded: {inventory} items.")