def load_inventory():
    try:
        with open("orders.txt", "r") as file:
            lines = file.readlines()
            history = []
            for line in lines:
                line = line.strip()
                if line:
                    parts = line.split(",")
                    order_id = int(parts[0].strip())
                    product_name = parts[1].strip()
                    quantity = int(parts[2].strip())
                    history.append((order_id, product_name, quantity))
        return history
    except (FileNotFoundError, ValueError, IndexError):
        return []


def save_inventory(history):
    with open("orders.txt", "w") as file:
        for order_id, product_name, quantity in history:
            file.write(f"{order_id}, {product_name}, {quantity}\n")


def display_current_orders(history):
    print("Current order:")
    for order_id, product_name, quantity in history:
        print(f"{order_id}, {product_name}, {quantity}")


def get_valid_input():
    product_name = input("\nEnter product name : ")
    if product_name.lower() == "quit":
        return "quit", None

    while True:
        quantity_input = input("Enter Quantity : ")
        if quantity_input.isdigit():
            return product_name, int(quantity_input)
        else:
            print("Error: please enter a valid whole number.")


def add_order(history, product_name, quantity):
    if history:
        last_id = history[-1][0]
        new_id = last_id + 1
    else:
        new_id = 1001

    new_order = (new_id, product_name, quantity)
    history.append(new_order)
    return new_order


def generate_report(history):
    print(f"\n--- Final Report ---")
    print(f"Total orders on record: {len(history)}")


def main():
    history = load_inventory()
    display_current_orders(history)

    while True:
        product_name, quantity = get_valid_input()

        if product_name == "quit":
            break

        new_order = add_order(history, product_name, quantity)

        print("\nNew order Added")
        print(f"{new_order[0]}, {new_order[1]}, {new_order[2]}")

        save_inventory(history)
        print("\nOrder successfully saved to orders.txt")

    generate_report(history)


if __name__ == "__main__":
    main()