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
    
def process_delivery(current_total, new_value):
    return current_total + new_value



def calculate_tax(amount):
    tax_rate = 0.1
    return amount * tax_rate


def generate_report(total_units, failed_attempts):
    print("\n--- Final Report ---")
    print(f"Total Deliveries Processed: {total_units}")
    print(f"Number of Failed/Rejected Entries: {failed_attempts}")
    
