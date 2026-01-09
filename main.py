def print_menu() -> None:
    print("\nWelcome to the Shopping CLI")
    print('1) Add Item')
    print('2) List Items')
    print('3) Remove Item')
    print('4) Total')
    print('0) Exit')

def main() -> None:
    items = []

    while True:
        print_menu()
        choice = input("Enter your choice: ").strip()
        if choice == "0":
            print("Goodbye!")
            break
        else:
            print("Not implemented yet: ",choice)

if __name__ == '__main__':
    main()