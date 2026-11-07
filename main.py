
from expense_manager import (
    add_expense,
    view_expenses,
    search_expenses,
    calculate_total_expenses,
    category_wise_summary,
    delete_expense
)

from csv_handler import load_expenses, save_expenses


def main():
    expenses = load_expenses()

    while True:
        print("\n===== EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Search Expenses by Category")
        print("4. Calculate Total Expenses")
        print("5. Category-wise Expense Summary")
        print("6. Delete an Expense")
        print("7. Exit")

        choice = input("\nEnter your choice (1-7): ")

        if choice == "1":
            add_expense(expenses)
            save_expenses(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            search_expenses(expenses)

        elif choice == "4":
            calculate_total_expenses(expenses)

        elif choice == "5":
            category_wise_summary(expenses)

        elif choice == "6":
            deleted = delete_expense(expenses)

            if deleted:
                save_expenses(expenses)

        elif choice == "7":
            print("Thank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice! Please enter a number between 1 and 7.")


if __name__ == "__main__":
    main()
