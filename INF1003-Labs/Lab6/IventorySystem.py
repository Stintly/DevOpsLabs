import json
import os
 
 
class Product: 
    def __init__(self, product_id: str, name: str, price: float, stock: int):
        self.__name = name
        self.__price = price
        self.__stock = stock
 

    def get_product_id(self) -> str:
        return self.__product_id
 
    def get_name(self) -> str:
        return self.__name
 
    def get_price(self) -> float:
        return self.__price
 
    def get_stock(self) -> int:
        return self.__stock

    def update_stock(self, quantity: int) -> bool:
        """Set the stock level to quantity.
 
        The Product decides how the value is treated: a negative quantity
        is rejected and the stock is left unchanged. Returns True if the
        stock was updated, False if it was rejected.
        """
        if quantity < 0:
            return False
        self.__stock = quantity
        return True
 
    def display_information(self) -> None:
        print(f"ID: {self.__product_id} | Name: {self.__name} | "
              f"Price: ${self.__price:.2f} | Stock: {self.__stock}")
 
 

class Inventory: 
    def __init__(self):
        self.__products = []  # holds Product objects
 
    def __find_by_id(self, product_id: str):
        """Private helper: exact (case-insensitive) match on product ID."""
        wanted = product_id.strip().lower()
        for product in self.__products:
            if product.get_product_id().lower() == wanted:
                return product
        return None
 
    def add_product(self, product) -> bool:
        """Add a product. Returns False if that ID is already in use."""
        if self.__find_by_id(product.get_product_id()) is not None:
            return False
        self.__products.append(product)
        return True
 
    def search_product(self, keyword: str):
        """Find a product by ID or by name (case-insensitive).
 
        Returns the Product, or None if nothing matches.
        """
        wanted = keyword.strip().lower()
        for product in self.__products:
            if (product.get_product_id().lower() == wanted
                    or product.get_name().lower() == wanted):
                return product
        return None
 
    def display_all(self) -> None:
        if len(self.__products) == 0:
            print("The inventory is empty.")
            return
        for product in self.__products:
            product.display_information()
 
    def get_products(self) -> list:
        """Return a copy of the product list, so outside code cannot
        add or remove items from the original list.
 
        This is a shallow copy: the list is new, but the Product objects
        inside it are the same objects.
        """
        return self.__products.copy()
 
 
INVENTORY_FILE = "inventory.json"
 
def read_field(record, *names):
    """Return the first matching field from a record (case-insensitive),
    or None if none of the names are present."""
    lowered = {key.lower(): value for key, value in record.items()}
    for name in names:
        if name in lowered:
            return lowered[name]
    return None
 
 
def load_inventory(inventory):
    """Read inventory.json into the Inventory object.
 
    If the file does not exist yet, start with an empty inventory
    instead of crashing.
    """
    if not os.path.exists(INVENTORY_FILE):
        return
 
    with open(INVENTORY_FILE, "r") as f:
        records = json.load(f)
 
    for record in records:
        product_id = read_field(record, "id", "product_id")
        name = read_field(record, "name")
        price = read_field(record, "price")
        stock = read_field(record, "stock", "quantity")
 
        if None in (product_id, name, price, stock):
            print("Skipped a record with missing fields:", record)
            continue
 
        product = Product(str(product_id), str(name), float(price), int(stock))
        inventory.add_product(product)
 
 
def save_inventory(inventory):
    """Write every product in the Inventory to inventory.json."""
    records = []
    for product in inventory.get_products():
        records.append({
            "id": product.get_product_id(),
            "name": product.get_name(),
            "price": product.get_price(),
            "stock": product.get_stock(),
        })
 
    with open(INVENTORY_FILE, "w") as f:
        json.dump(records, f, indent=4)
 
def ask_whole_number(prompt):
    while True:
        text = input(prompt).strip()
        if text.isdigit():
            return int(text)
        print("Please enter a whole number (0 or more).")
 
 
def ask_price(prompt):
    while True:
        text = input(prompt).strip()
        # allow at most one decimal point, e.g. 12.50
        if text.replace(".", "", 1).isdigit():
            return float(text)
        print("Please enter a valid price, e.g. 12.50.")
 
 
def add_product_action(inventory):
    product_id = input("Product ID: ").strip()
    name = input("Product name: ").strip()
    if product_id == "" or name == "":
        print("ID and name cannot be empty.")
        return
 
    price = ask_price("Price: ")
    stock = ask_whole_number("Stock quantity: ")
 
    product = Product(product_id, name, price, stock)
    if inventory.add_product(product):
        print("Product added.")
    else:
        print("A product with that ID already exists.")
 
 
def update_stock_action(inventory):
    keyword = input("Product ID or name: ").strip()
    product = inventory.search_product(keyword)
    if product is None:
        print("Product not found.")
        return
 
    quantity = ask_whole_number("New stock quantity: ")
    if product.update_stock(quantity):
        print("Stock updated.")
    else:
        print("Stock was not updated.")
 
 
def search_action(inventory):
    keyword = input("Product ID or name: ").strip()
    product = inventory.search_product(keyword)
    if product is None:
        print("Product not found.")
    else:
        product.display_information()
 
 
def print_menu():
    print("\n===== Inventory Management =====")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
 

def main():
    inventory = Inventory()
    load_inventory(inventory)
 
    while True:
        print_menu()
        choice = input("Choose an option (1-6): ").strip()
 
        if choice == "1":
            inventory.display_all()
        elif choice == "2":
            add_product_action(inventory)
        elif choice == "3":
            update_stock_action(inventory)
        elif choice == "4":
            search_action(inventory)
        elif choice == "5":
            save_inventory(inventory)
            print("Inventory saved.")
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")
 
 
if __name__ == "__main__":
    main()