# Expense Tracker Application
# Developed using Python
# Internship Organization: CodeOrbit Tech

from expense_manager import add_expense


def main():

    # Stores expenses temporarily in a list
    expenses = []

    while True:

        print("\n========================================")
        print("           EXPENSE TRACKER")
        print("========================================")

        print("1. Add Expense")
        print("2. Exit")

        print("========================================")

        choice = input("Enter your choice (1-2): ")

        if choice == "1":

            # Call the add expense function
            add_expense(expenses)

        elif choice == "2":

            print("\nThank you for using Expense Tracker!")
            print("Exiting application...")
            break

        else:

            print("\nInvalid choice! Please select 1 or 2.")


# Start the application
if __name__ == "__main__":
    main()