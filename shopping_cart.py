# Description: Define a class ShoppingCart with an attribute items (a list of dictionaries with
# name, price, and quantity). Include methods add_item(name, price, quantity),
# remove_item(name), and total_cost() to calculate the total cost of items in the cart.
# Task: Create an instance of the ShoppingCart class, add and remove items, and display
# the total cost

class ShoppingCart:
    def __init__(self, items = {}) -> None:
        self.items = items
    
    def add_item(self, name, price, quantity):
        for item in self.items:
            if (item["name"] == name):
                item["quantity"] += quantity
                return
        item = {"name": name, "price": price, "quantity": quantity}
        self.items.append(item)

    def remove_item(self, name):
        self.items = [item for item in self.items if (item["name"] == name)]
        return self.items

    def total_cost(self):
        return sum([item["price"] * item["quantity"] for item in self.items])
    
cart = ShoppingCart([
    {"name": "USB Drive", "price": 3_000, "quantity": 2},
    {"name": "Laptop Charger", "price": 9_000, "quantity": 1}
])

cart.add_item("USB Drive", 3_000, 1)
print(f"Total cost: {cart.total_cost()}")

cart.remove_item("USB Drive")
print(f"Total cost: {cart.total_cost()}")