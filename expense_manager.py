# This file will manage expense-related operations.
# Expense Manager
# Handles expense-related operations.

from datetime import date


def add_expense(expenses):
    """
    Takes expense details from the user
    and adds a new expense to the list.
    """

    print("\n========== ADD NEW EXPENSE ==========")

    # Generate a unique expense ID
    expense_id = len(expenses) + 1

    # Get today's date automatically
    expense_date = date.today().strftime("%Y-%m-%d")

    # Take category from the user
    while True:
        category = input("Enter category: ").strip()

        if category:
            break

        print("Category cannot be empty.")

    # Take expense description
    while True:
        description = input("Enter description: ").strip()

        if description:
            break

        print("Description cannot be empty.")

    # Take and validate expense amount
    while True:
        try:
            amount = float(input("Enter amount: "))

            if amount > 0:
                break

            print("Amount must be greater than zero.")

        except ValueError:
            print("Please enter a valid numeric amount.")

    # Create expense record
    expense = {
        "ID": expense_id,
        "Date": expense_date,
        "Category": category,
        "Description": description,
        "Amount": amount
    }

    # Add expense to the list
    expenses.append(expense)

    print("\nExpense added successfully!")
    print(f"Expense ID: {expense_id}")