# oughlane
# File: shopping_list_manager.py

# Function to display the menu
def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

# Main function
def main():
    # Array to store the shopping list
    shopping_list = []

    while True:
        # Call the menu display function
        display_menu()

        try:
            # Get user's choice as a number
            choice = int(input("Enter your choice (1-4): "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print(f"{item} added.")

        elif choice == 2:
            item = input("Enter the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"{item} removed.")
            else:
                print("Item not found.")

        elif choice == 3:
            if shopping_list:
                print("Shopping List:")
                for i, item in enumerate(shopping_list, 1):
                    print(f"{i}. {item}")
            else:
                print("The list is empty.")

        elif choice == 4:
            print("Goodbye.")
            break
        else:
            print("Invalid choice. Try again.")

# Entry point
if __name__ == "__main__":
    main()
