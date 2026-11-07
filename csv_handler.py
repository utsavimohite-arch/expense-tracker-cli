
import csv
import os
import math

FILE_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "expenses.csv"
)

FIELDNAMES = ["ID", "Date", "Category", "Description", "Amount"]


def save_expenses(expenses):
    try:
        with open(FILE_PATH, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
            writer.writeheader()

            for expense in expenses:
                writer.writerow({
                    "ID": expense["ID"],
                    "Date": expense["Date"],
                    "Category": expense["Category"],
                    "Description": expense["Description"],
                    "Amount": expense["Amount"]
                })

        print("Expenses saved successfully.")
        return True

    except (OSError, csv.Error, ValueError, KeyError) as error:
        print(f"Error saving expenses: {error}")
        return False


def load_expenses():
    expenses = []

    if not os.path.exists(FILE_PATH):
        print("CSV file not found. Creating a new expense file.")
        save_expenses(expenses)
        return expenses

    try:
        with open(FILE_PATH, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            if reader.fieldnames is None:
                print("CSV file is empty. Starting with no expenses.")
                return expenses

            missing_columns = [
                field for field in FIELDNAMES
                if field not in reader.fieldnames
            ]

            if missing_columns:
                print("Error: CSV file has an incorrect format.")
                print(f"Missing columns: {', '.join(missing_columns)}")
                return expenses

            seen_ids = set()
            skipped_records = 0

            for row in reader:
                try:
                    expense_id = int(row["ID"])
                    amount = float(row["Amount"])

                    if expense_id <= 0 or expense_id in seen_ids:
                        raise ValueError("Invalid or duplicate expense ID")

                    if not math.isfinite(amount) or amount <= 0:
                        raise ValueError("Invalid expense amount")

                    if not row["Date"].strip():
                        raise ValueError("Missing date")

                    if not row["Category"].strip():
                        raise ValueError("Missing category")

                    if not row["Description"].strip():
                        raise ValueError("Missing description")

                    expense = {
                        "ID": expense_id,
                        "Date": row["Date"].strip(),
                        "Category": row["Category"].strip(),
                        "Description": row["Description"].strip(),
                        "Amount": amount
                    }

                    expenses.append(expense)
                    seen_ids.add(expense_id)

                except (ValueError, TypeError, KeyError):
                    skipped_records += 1

            if skipped_records:
                print(
                    f"Warning: {skipped_records} invalid CSV record(s) "
                    "were skipped."
                )

    except (OSError, csv.Error, UnicodeDecodeError) as error:
        print(f"Error reading expenses.csv: {error}")
        return []

    return expenses
