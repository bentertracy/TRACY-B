# inventory_system.py

# List to store product dictionaries
inventory = []

# Input for five items
for i in range(5):
    print(f"\nEnter details for item {i+1}:")
    name = input("Product Name: ")
    quantity = int(input("Quantity: "))
    price = float(input("Unit Price: "))

    item = {
        "name": name,
        "quantity": quantity,
        "price": price
    }
    inventory.append(item)

# Display table header
print("\n----------------- INVENTORY REPORT -----------------")
print("{:<20} {:<10} {:<10} {:<10}".format("Product", "Quantity", "Unit Price", "Total Value"))
print("-----------------------------------------------------")

grand_total = 0

# Display each item and compute totals
for item in inventory:
    total_value = item["quantity"] * item["price"]
    grand_total += total_value

    print("{:<20} {:<10} {:<10.2f} {:<10.2f}".format(
        item["name"],
        item["quantity"],
        item["price"],
        total_value
    ))

# Display grand total
print("-----------------------------------------------------")
print(f"GRAND TOTAL VALUE: {grand_total:.2f}")