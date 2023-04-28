class Item:
    def __init__(self, code, name, price):
        self.code = code
        self.name = name
        self.price = price

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

items = []
while True:
    code = input("Enter item code: ")
    name = input("Enter item name: ")
    price = get_float_input("Enter item price: $")

    items.append(Item(code, name, price))

    add_another = input("Add another item? (Y/N): ")
    if add_another.lower() != "y":
        break

print("ITEMS PURCHASED:")
print("Code\tName\tPrice")
for item in items:
    print(f"{item.code}\t{item.name}\t${item.price:.2f}")

total = sum(item.price for item in items)
print(f"TOTAL PRICE: ${total:.2f}")