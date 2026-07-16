from operations import (
    add_expense, 
    view_expense, 
    delete_expense, 
    search_expense, 
    calculate_total, 
    filter_by_category
)

def main():
    print("--- Welcome to Your Personal Expense Tracker! ---")
    
    while True:
        # 2. Display the Interactive Menu Options
        print("\nWhat would you like to do?")
        print("1. Add an Expense")
        print("2. View All Expenses")
        print("3. Delete an Expense")
        print("4. Search for an Expense")
        print("5. Calculate Total Spending")
        print("6. Filter Expenses by Category")
        print("7. Exit Application")
        
        choice = input("Enter your choice (1-7): ").strip()
        print("-" * 40) # Simple visual separator line

        # 3. Route the user's choices to your functions
        if choice == "1":
            title = input("Enter expense title: ")
            amount = input("Enter amount: ")
            category = input("Enter category: ")
            # Call your add function (it handles the auto-date formatting internally)
            result = add_expense(title, amount, category)
            print(result)

        elif choice == "2":
            lines = view_expense()
            for line in lines:
                print(line)

        elif choice == "3":
            title = input("Enter the title of the expense to delete: ")
            results = delete_expense(title)
            # Since delete_expense returns a list with a message, print it out
            for line in results:
                print(line)

        elif choice == "4":
            title = input("Enter the expense title to search for: ")
            result = search_expense(title)
            print(result)

        elif choice == "5":
            result = calculate_total()
            print(result)

        elif choice == "6":
            category = input("Enter the category to filter by: ")
            lines = filter_by_category(category)
            for line in lines:
                print(line)

        elif choice == "7":
            print("Goodbye! Thanks for tracking your expenses.")
            break # Breaks the while loop to safely close the app

        else:
            print("Invalid choice! Please type a number between 1 and 7.")


if __name__ == "__main__":
    main()
