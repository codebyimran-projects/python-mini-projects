# Menu items and their prices stored in a dictionary
items = {
    'tea': 90,
    'pepsi': 100,
    'coke': 110,
    'coffee': 120,
    'juice': 130,
    'water': 80
}

# An empty list to store items the customer orders
customer_cart = []

# Welcome message
print("Welcome to the Annie Cafe!")
print("Here is our menu:\n")

# Display the menu using a loop
for item, price in items.items():
    print(f"{item}: ${price}")

# Variable to control if the customer wants to order more
wants_more = True

# Loop keeps running until customer says "no"
while wants_more:
    # Ask for item name
    customer = input("\nWhat would you like to order, Sir?: ").lower()

    # Check if the entered item exists in our menu
    if customer in items:
        # Add the item to the customer's cart
        customer_cart.append(customer)
        print(f"{customer.capitalize()} has been added to your cart.")
    else:
        print("Sorry, we don't have that item.")

    # Ask if the customer wants to order more
    ask_more = input("Do you want to order anything else? (yes/no): ").lower()

    # If no, stop the loop and show final bill
    if ask_more == 'no':
        wants_more = False
        print("\nThank you for your order. Here is your bill:")
        print("-" * 35)

        # Display all ordered items with prices
        total = 0
        for item in customer_cart:
            print(f"{item.capitalize()}: ${items[item]}")
            total += items[item]

        print("-" * 35)
        print(f"Total amount: ${total}")
        print("Have a great day!")
