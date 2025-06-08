shopping_list = []


def add_items(shopping_list):
    item = input("What item do you want to get?: ")
    if item:
        shopping_list.append(item)
        print(f"'{item}' has been added to your shopping list.")
    else:
        print("Item name cannot be empty.")


def remove_items(shopping_list):
    item = input("What item do you want to remove?: ")
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"'{item}' has been removed from your shopping list.")
    else:
        print(f"'{item}' not found in your shopping list.")

def view_list(shopping_list):
    if not shopping_list:
         print("Your shopping list is empty.")
    else:
        print("\n🛒 Your Shopping List:")
        for index, item in enumerate(shopping_list, start=1):
            print(f"{index}. {item}")
            
def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = int(input("Enter your choice: "))

        if choice == '1':
            add_items(shopping_list)
            pass
        elif choice == '2':
            remove_items(shopping_list)
            pass
        elif choice == '3':
            view_list(shopping_list)
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
