#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import json

def load_data():
    try:
        with open('data.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {'products': [], 'sales': []}

def save_data(data):
    with open('data.json', 'w') as file:
        json.dump(data, file)

def add_product(inventory, name, quantity, purchase_price, selling_price):
    for product in inventory:
        if product['name'] == name:
            product['quantity'] += quantity
            return
    new_product = {
        'name': name,
        'quantity': quantity,
        'purchase_price': purchase_price,
        'selling_price': selling_price
    }
    inventory.append(new_product)

def list_products(inventory):
    print("PRODUCT QUANTITY PRICE")
    for product in inventory:
        print(f"{product['name']} {product['quantity']} ${product['selling_price']:.2f}")

def record_sale(inventory, sales, name, quantity):
    for product in inventory:
        if product['name'] == name:
            if product['quantity'] >= quantity:
                sales.append({
                    'name': name,
                    'quantity': quantity,
                    'selling_price': product['selling_price']
                })
                product['quantity'] -= quantity
                return True
            else:
                print(f"Error: Insufficient quantity of {name} in the inventory.")
                return False
    print(f"Error: Product {name} not found in the inventory.")
    return False

def calculate_profits(sales, inventory):
    gross_profit = sum(sale['quantity'] * sale['selling_price'] for sale in sales)
    purchase_cost = sum(sale['quantity'] * product['purchase_price'] for sale in sales for product in inventory)
    net_profit = gross_profit - purchase_cost
    return gross_profit, net_profit

def show_help():
    print("Available commands are:")
    print("- add: add a product to the inventory")
    print("- list: list products in the inventory")
    print("- sale: record a sale")
    print("- profits: display total profits")
    print("- help: show available commands")
    print("- exit: exit the program")

def main():
    data = load_data()
    inventory = data['products']
    sales = data['sales']

    cmd = None

    while cmd != "exit":
        cmd = input("Enter a command: ")

        if cmd == "add":
            product_name = input("Product name: ")
            quantity = int(input("Quantity: "))
            purchase_price = float(input("Purchase price: "))
            selling_price = float(input("Selling price: "))
            add_product(inventory, product_name, quantity, purchase_price, selling_price)
            print(f"ADDED: {quantity} X {product_name}")

        elif cmd == "list":
            list_products(inventory)

        elif cmd == "sale":
            while True:
                product_name = input("Product name: ")
                quantity = int(input("Quantity: "))
                if record_sale(inventory, sales, product_name, quantity):
                    print("SALE RECORDED")
                another_product = input("Add another product? (yes/no): ")
                if another_product.lower() != "yes":
                    break

        elif cmd == "profits":
            gross_profit, net_profit = calculate_profits(sales, inventory)
            print(f"Profits: gross=${gross_profit:.2f} net=${net_profit:.2f}")

        elif cmd == "help":
            show_help()

        elif cmd == "exit":
            save_data({'products': inventory, 'sales': sales})
            print("Bye bye")

        else:
            print("Invalid command")
            show_help()

if __name__ == "__main__":
    main()
    


# In[ ]:




