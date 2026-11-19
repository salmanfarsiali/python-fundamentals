
# ==================================================
# Project: Online Shopping Cart System
# Using Object-Oriented Programming (OOP)
# ==================================================


# Part A: Class Creation
# Create a class named ShoppingCart with the following:
# Attributes:
# - customer_name → Name of the customer (string)
# - items → List of item prices (list of numbers)
# Constructor:
# - Use init() to initialize all attributes correctly
# - If no items are provided, initialize with an empty list

class ShoppingCart:

    def __init__(self, customer_name, items=None):
        self.customer_name = customer_name
        self.items = list(items) if items is not None else []


    # Part B: Core Methods
    

    # 1. Add item
    def add_item(self, price):
        if isinstance(price, (int, float)) and not isinstance(price, bool) and price > 0:
            self.items.append(price)
            print(f"Item price {price} added successfully.")
        else:
            print("Invalid price! Price must be a positive number.")


    # 2. Remove item
    def remove_item(self, price):
        if price in self.items:
            self.items.remove(price)
            print(f"Item price {price} removed successfully.")
        else:
            print(f"Item price {price} not found in the cart.")


    # 3. Calculate total
    def calculate_total(self):
        total = 0

        for price in self.items:
            total += price

        return total


    # 4. Apply discount
    def apply_discount(self):
        total = self.calculate_total()

        if total >= 3000:
            discount = total * 0.10
            final_amount = total - discount
            return final_amount
        else:
            return total


    # Part C: Display & Utility Methods

    # 1. Display cart details
    def display_cart(self):

        print("\n========== Shopping Cart ==========")

        print("Customer Name :", self.customer_name)
        print("Items         :", self.items)
        print("Total Amount  :", self.calculate_total())
        print("Payable Amount:", self.apply_discount())
        print("Number of Items:", len(self.items))

        print("===================================")


    # 2. Clear cart
    def clear_cart(self):
        self.items.clear()
        print(f"{self.customer_name}'s cart has been cleared successfully.")


    # Part D: Combine Two Shopping Carts

    def __add__(self, other):

        if not isinstance(other, ShoppingCart):
            return NotImplemented

        combined_customer = (
            self.customer_name + " & " + other.customer_name
        )

        combined_items = self.items + other.items

        return ShoppingCart(combined_customer, combined_items)


# ==================================================
# Part D: Object Usage & Testing
# ==================================================


# 1. Create two ShoppingCart objects

cart1 = ShoppingCart("Salman")
cart2 = ShoppingCart("Rahim")


# 2. Add items to Cart 1

print("\n----- Adding Items to Cart 1 -----")

cart1.add_item(1500)
cart1.add_item(1200)
cart1.add_item(800)


# 3. Add items to Cart 2

print("\n----- Adding Items to Cart 2 -----")

cart2.add_item(1000)
cart2.add_item(900)
cart2.add_item(700)


# 4. Remove items from both carts

print("\n----- Removing Items -----")

cart1.remove_item(800)
cart2.remove_item(900)


# 5. Display individual cart details

print("\n----- Cart 1 Details -----")
cart1.display_cart()

print("\n----- Cart 2 Details -----")
cart2.display_cart()


# 6. Combine both carts using +

print("\n----- Combining Both Carts -----")

combined_cart = cart1 + cart2


# 7. Display combined cart details

print("\n----- Combined Cart Details -----")
combined_cart.display_cart()


# 8. Test clear_cart() method

print("\n----- Clearing Cart 1 -----")

cart1.clear_cart()

cart1.display_cart()
