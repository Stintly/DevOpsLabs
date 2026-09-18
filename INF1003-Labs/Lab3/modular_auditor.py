def get_valid_input():
    fail_count = 0
    while True:
        user_input = input("Enter stock quantity (or 'quit' to finish): ")

        if user_input.lower() == "quit":
            return "quit", fail_count

        if not user_input.isdigit():
            print("Error: please enter a valid whole number.")
            fail_count += 1
            continue

        return int(user_input), fail_count

    
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


        if total_inventory > 500:
            print(f"ALERT: Overstock! Total inventory ({total_inventory}) exceeds 500 units.")
            break

        elif total_inventory == 500:
            print("Notice: Inventory has reached exactly 500 units.")
            
        else:
            print(f"Current total inventory: {total_inventory}")

        
        
    generate_report(deliveries_count, failed_attempts)


if __name__ == "__main__":
    main()