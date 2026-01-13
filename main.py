import json
from pathlib import Path

DATA_FILE = Path("items.json")

def load_items() -> list:
    if not DATA_FILE.exists():
        return []
    try:
        with DATA_FILE.open("r", encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, list):
            return data
    except (json.JSONDecoderError, OSError):
        pass

    print("Warning: items.json could not be loaded. Starting with an empty list.")
    return []

def save_items(items: list) -> None:
    try:
        with DATA_FILE.open("w", encoding="utf-8") as f:
            json.dump(items, f, ensure_ascii=False, indent=2)
    except OSError:
        print("Warning: items.json could not be saved")

def print_menu() -> None:
    print_line()
    print("Welcome to the Shopping CLI")
    print_line()
    print('1) Add Item')
    print('2) List Items')
    print('3) Remove Item')
    print('4) Total')
    print('0) Exit')

def print_line() -> None:
    print('-'*30)

def add_item(items: list) -> None:
    name = input("Item name: ").strip()
    try:
        qty = int(input("Quantity: ").strip())
        price = float(input("Price: ").strip())
    except ValueError:
        print("Quantity must be integer and price must be a number.")
        return

    item = {
        "name": name,
        "qty": qty,
        "price": price
    }

    items.append(item)
    save_items(items)
    print("Item added successfully!")

    print("You entered: ")
    print("Name: ",name)
    print("Quantity: ",qty)
    print("Price: ",price)

def list_items(items: list) -> None:
    if not items:
        print("No items added!")
        return
    print_line()
    for index, item in enumerate(items, start=1):
        print(f"{index}. {item['name']} - {item['qty']} * {item['price']}")
    print_line()

def remove_item(items: list) -> None:
    if not items:
        print("No items added!")
        return
    list_items(items)

    try:
        index = int(input("Enter item to remove: ").strip())
    except ValueError:
        print("Please enter a valid number.")
        return

    if index < 1 or index > len(items):
        print("Invalid item number.")
        return

    removed_item = items.pop(index-1)
    save_items(items)
    print(f"Item removed: {removed_item['name']}")

def calculate_total(items: list) -> None:
    if not items:
        print("No items to calculate!")
        return
    total = 0.0
    for item in items:
        total += item['qty'] * item['price']
    print_line()
    print(f"Total amount: {total}")
    print_line()

def main() -> None:
    items = load_items()
    running = True

    while running:
        print_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_item(items)
        elif choice == "2":
            list_items(items)
        elif choice == "3":
            remove_item(items)
        elif choice == "4":
            calculate_total(items)
        elif choice == "0":
            save_items(items)
            print("Goodbye!")
            break
        else:
            print("Please enter a valid choice")

if __name__ == '__main__':
    main()