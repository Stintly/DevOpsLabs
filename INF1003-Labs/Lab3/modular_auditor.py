inventory = 0

def get_valid_input():
    while True:
        user_input = input("Enter the number of items to add to inventory (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            return "quit", 0

        if not user_input.isdigit():
            print("Please enter a valid number.")
            continue

        return int(user_input)
    
def process_delivery(current_total, new_value):
    return current_total + new_value



def calculate_tax(amount):
    tax_rate = 0.1
    return amount * tax_rate


def generate_report(total_units, failed_attempts):
    print("\n--- Final Report ---")
    print(f"Total Deliveries Processed: {total_units}")
    print(f"Number of Failed/Rejected Entries: {failed_attempts}")
    

def main():
    total_inventory = 0
    deliveries_count = 0
    failed_attempts = 0

    while True:
        value, fails = get_valid_input()
        failed_attempts += fails

        if value == "quit":
            break

        total_inventory = process_delivery(total_inventory, value)
        tax = calculate_tax(value)
        deliveries_count += 1

        print(f"Delivery recorded: {value} units | Tax on this delivery: {tax:.2f} | Running total: {total_inventory}")

    generate_report(deliveries_count, failed_attempts)


if __name__ == "__main__":
    main()