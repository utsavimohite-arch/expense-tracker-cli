
from datetime import date
import math


def add_expense(expenses):
    print("\n===== ADD EXPENSE =====")

    category = input("Enter category (e.g., Food, Travel): ").strip()

    if not category:
        print("Error: Category cannot be empty!")
        return

    description = input("Enter description: ").strip()

    if not description:
        print("Error: Description cannot be empty!")
        return

    try:
        amount = float(input("Enter amount: "))

        if not math.isfinite(amount):
            print("Error: Please enter a finite amount!")
            return

        if amount <= 0:
            print("Error: Amount must be greater than zero!")
            return

    except ValueError:
        print("Error: Please enter a valid numeric amount!")
        return

    expense_id = max(
        (expense["ID"] for expense in expenses),
        default=0
    ) + 1

    expense = {
        "ID": expense_id,
        "Date": date.today().strftime("%Y-%m-%d"),
        "Category": category,
        "Description": description,
        "Amount": amount
    }

    expenses.append(expense)
    print("\nExpense added successfully!")


def view_expenses(expenses):
    print("\n===== ALL EXPENSES =====")

    if not expenses:
        print("No expenses found!")
        return

    print("-" * 75)
    print(
        f"{'ID':<5}{'Date':<15}{'Category':<15}"
        f"{'Description':<20}{'Amount':>12}"
    )
    print("-" * 75)

    for expense in expenses:
        print(
            f"{expense['ID']:<5}"
            f"{expense['Date']:<15}"
            f"{expense['Category']:<15}"
            f"{expense['Description']:<20}"
            f"{expense['Amount']:>12.2f}"
        )

    print("-" * 75)


def search_expenses(expenses):
    print("\n===== SEARCH EXPENSES =====")

    if not expenses:
        print("No expenses available to search!")
        return

    category = input("Enter category to search: ").strip()

    if not category:
        print("Error: Please enter a category!")
        return

    results = [
        expense for expense in expenses
        if expense["Category"].casefold() == category.casefold()
    ]

    if not results:
        print("No expenses found in this category!")
        return

    print(f"\nExpenses in category: {category}")
    print("-" * 75)

    for expense in results:
        print(
            f"ID: {expense['ID']} | "
            f"Date: {expense['Date']} | "
            f"Description: {expense['Description']} | "
            f"Amount: {expense['Amount']:.2f}"
        )

    print("-" * 75)


def calculate_total_expenses(expenses):
    print("\n===== TOTAL EXPENSES =====")

    if not expenses:
        print("No expenses recorded yet!")
        return

    total = sum(expense["Amount"] for expense in expenses)

    print(f"Total number of expenses: {len(expenses)}")
    print(f"Total amount spent: {total:.2f}")


def category_wise_summary(expenses):
    print("\n===== CATEGORY-WISE EXPENSE SUMMARY =====")

    if not expenses:
        print("No expenses recorded yet!")
        return

    category_totals = {}

    for expense in expenses:
        category = expense["Category"].strip().title()
        amount = float(expense["Amount"])

        category_totals[category] = (
            category_totals.get(category, 0) + amount
        )

    print("-" * 45)

    for category, total in sorted(category_totals.items()):
        print(f"{category:<25}: Rs. {total:.2f}")

    print("-" * 45)

    grand_total = sum(category_totals.values())

    print(f"{'Grand Total':<25}: Rs. {grand_total:.2f}")
    print("-" * 45)


def delete_expense(expenses):
    print("\n===== DELETE EXPENSE =====")

    if not expenses:
        print("No expenses available to delete!")
        return False

    view_expenses(expenses)

    try:
        expense_id = int(input("\nEnter the Expense ID to delete: "))

        if expense_id <= 0:
            print("Error: Expense ID must be positive!")
            return False

    except ValueError:
        print("Error: Please enter a valid numeric ID!")
        return False

    for expense in expenses:
        if expense["ID"] == expense_id:
            print("\nExpense found:")
            print(f"Category: {expense['Category']}")
            print(f"Description: {expense['Description']}")
            print(f"Amount: {expense['Amount']:.2f}")

            confirmation = input(
                "\nAre you sure you want to delete this expense? "
                "(yes/no): "
            ).strip().lower()

            if confirmation == "yes":
                expenses.remove(expense)
                print("\nExpense deleted successfully!")
                return True

            print("\nDeletion cancelled.")
            return False

    print("\nNo expense found with that ID!")
    return False
