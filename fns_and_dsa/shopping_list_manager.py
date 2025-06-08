# oughlane
# shopping_list_manager.py

# Function to display the menu options
def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Clear All Items")
    print("5. Exit")

# Main function to handle logic
def main():
    shopping_list = []

    while True:
        display_menu()

        try:
            choice = int(input("Enter your choice (1-5): "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print(f"'{item}' has been added.")

        elif choice == 2:
            item = input("Enter the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed.")
            else:
                print("Item not found.")

        elif choice == 3:
            if not shopping_list:
                print("The shopping list is empty.")
            else:
                print("Shopping List:")
                for i, article in enumerate(shopping_list, 1):
                    print(f"{i}. {article}")

        elif choice == 4:
            shopping_list.clear()
            print("All items have been cleared.")

        elif choice == 5:
            print("Goodbye.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
