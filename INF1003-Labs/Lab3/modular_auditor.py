inventory = 0

def get_valid_input():
    while True:
        user_input = input("Enter the number of items to add to inventory (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            return None

        if not user_input.isdigit():
            print("Please enter a valid number.")
            continue

        return int(user_input)
