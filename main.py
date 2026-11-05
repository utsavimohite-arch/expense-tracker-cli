# Expense Tracker Application
# Developed using Python
# Internship Organization: CodeOrbit Tech

from expense_manager import add_expense
from csv_handler import load_expenses, save_expenses


def main():

    # Load previously saved expenses
    expenses = load_expenses()

    while True:

        print("\n========================================")
        print("           EXPENSE TRACKER")
        print("========================================")

        print("1. Add Expense")
        print("2. Exit")

        print("========================================")

        choice = input("Enter your choice (1-2): ")

        if choice == "1":

            # Add a new expense
            add_expense(expenses)

            # Save updated expenses into CSV
            save_expenses(expenses)

        elif choice == "2":

            print("\nThank you for using Expense Tracker!")
            print("Exiting application...")
            break

        else:

            print("\nInvalid choice! Please select 1 or 2.")


# Start the application
if __name__ == "__main__":
    main()