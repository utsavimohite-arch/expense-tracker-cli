
# Expense Manager
# Handles all expense-related operations.
# Project: Expense Tracker Application
# Organization: CodeOrbit Tech

from datetime import date


def add_expense(expenses):
    """
    Takes expense details from the user
    and adds a new expense to the list.
    """

    print("\n========== ADD NEW EXPENSE ==========")

    # Generate a unique expense ID
    if expenses:
        expense_id = max(expense["ID"] for expense in expenses) + 1
    else:
        expense_id = 1

    # Get today's date automatically
    expense_date = date.today().strftime("%Y-%m-%d")

    # Get category
    while True:
        category = input("Enter category: ").strip()

        if category:
            break

        print("Category cannot be empty.")

    # Get description
    while True:
        description = input("Enter description: ").strip()

        if description:
            break

        print("Description cannot be empty.")

    # Get and validate amount
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


def view_expenses(expenses):
    """
    Displays all recorded expenses.
    """

    print("\n========== ALL EXPENSES ==========")

    if not expenses:
        print("No expenses recorded yet.")
        return

    print("-" * 85)

    print(
        f"{'ID':<5}"
        f"{'Date':<15}"
        f"{'Category':<15}"
        f"{'Description':<25}"
        f"{'Amount':>12}"
    )

    print("-" * 85)

    for expense in expenses:
        print(
            f"{expense['ID']:<5}"
            f"{expense['Date']:<15}"
            f"{expense['Category']:<15}"
            f"{expense['Description']:<25}"
            f"{expense['Amount']:>12.2f}"
        )

    print("-" * 85)


def search_expenses(expenses):
    """
    Searches expenses using their category.
    """

    print("\n========== SEARCH EXPENSES ==========")

    if not expenses:
        print("No expenses available to search.")
        return

    search_category = input("Enter category to search: ").strip()

    if not search_category:
        print("Category cannot be empty.")
        return

    found_expenses = []

    for expense in expenses:
        if expense["Category"].lower() == search_category.lower():
            found_expenses.append(expense)

    if found_expenses:

        print("\nMatching Expenses:")

        for expense in found_expenses:
            print("-" * 40)
            print(f"ID: {expense['ID']}")
            print(f"Date: {expense['Date']}")
            print(f"Category: {expense['Category']}")
            print(f"Description: {expense['Description']}")
            print(f"Amount: Rs. {expense['Amount']:.2f}")

    else:
        print("No expenses found in this category.")
