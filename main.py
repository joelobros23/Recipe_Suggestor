# main.py - Created by AI Programmer

def display_menu():
    print("Recipe Suggestion App")
    print("-----------------------")
    print("1. Enter available ingredients")
    print("2. Get recipe suggestions")
    print("3. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            print("Enter ingredients (separated by commas):")
            ingredients = input()
            # TODO: Store ingredients

        elif choice == '2':
            # TODO: Suggest recipes based on stored ingredients
            print("Recipe suggestions coming soon!")

        elif choice == '3':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()