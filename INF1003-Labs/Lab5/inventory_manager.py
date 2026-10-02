import json
import os


def find_product(inventory, product_id):
    for product in inventory:
        if product["id"] == product_id:
            return product
    return None


def load_inventory():
    if os.path.exists("inventory.json"):
        print("inventory.json found.")
        with open("inventory.json", "r") as file:
            inventory = json.load(file)
        print("Inventory loaded successfully.")
        return inventory
    else:
        print("inventory.json not found. Starting with an empty inventory.")
        return []

def save_inventory(inventory):
    with open("inventory.json", "w") as file:
        json.dump(inventory, file, indent=4)
    print("Inventory saved successfully to inventory.json.")


def add_product(inventory):
    print("Add New Product")
    product_id = input("Product ID: ")
    name = input("Product Name: ")
    price = float(input("Price: "))
    stock = int(input("Stock Quantity: "))

    new_product = {
        "id": product_id,
        "name": name,
        "price": price,
        "stock": stock
    }

    inventory.append(new_product)
    print("Product added successfully!")


def update_stock(inventory):
    print("Update Stock")
    product_id = input("Enter Product ID: ")
    product = find_product(inventory, product_id)

    if product is None:
        print("Product not found.")
    else:
        print("Product Found:")
        print(f"Name: {product['name']}")
        print(f"Current Stock: {product['stock']}")
        new_stock = int(input("New Stock Quantity: "))
        product["stock"] = new_stock
        print("Stock updated successfully!")

def display_all(inventory):
    print("Current Inventory")
    print("------------------------------------------------")
    for product in inventory:
        print(f"ID: {product['id']} | Name: {product['name']} | Price: ${product['price']:.2f} | Stock: {product['stock']}")
    print("------------------------------------------------")


def search_product(inventory):
    print("Search Product")
    product_id = input("Enter Product ID: ")
    product = find_product(inventory, product_id)

    if product is None:
        print("Product not found.")
    else:
        print("Product Found")
        print("------------------------------------------------")
        print(f"ID: {product['id']}")
        print(f"Name: {product['name']}")
        print(f"Price: ${product['price']:.2f}")
        print(f"Stock: {product['stock']}")
        print("------------------------------------------------")
