# student_records.py

# Open file to write
file = open("records.txt", "w")

for i in range(3):
    name = input(f"Enter name of student {i+1}: ")
    score = input(f"Enter score for {name}: ")

    file.write(name + " - " + score + "\n")

file.close()

print("Student records saved to records.txt")


# ---------------------------------------------------------
# READ BACK THE DATA
# ---------------------------------------------------------

print("\n----------------- INVENTORY REPORT -----------------")
print("{:<20} {:<10} {:<10} {:<12}".format("Product", "Quantity", "Unit Price", "Total Value"))
print("-----------------------------------------------------")

grand_total = 0

with open("inventory.txt", "r") as file:
    for line in file:
        name, quantity, price = line.strip().split(",")
        quantity = int(quantity)
        price = float(price)
        total_value = quantity * price
        grand_total += total_value

        print("{:<20} {:<10} {:<10.2f} {:<12.2f}".format(
            name, quantity, price, total_value
        ))

print("-----------------------------------------------------")
print(f"GRAND TOTAL VALUE: {grand_total:.2f}")