# This file will handle CSV file operations.
# CSV Handler
# Handles saving and loading expense records.

import csv
import os

# Get the location of the CSV file
FILE_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "expenses.csv"
)


def save_expenses(expenses):
    """
    Saves all expense records into the CSV file.
    """

    fieldnames = [
        "ID",
        "Date",
        "Category",
        "Description",
        "Amount"
    ]

    with open(FILE_PATH, mode="w", newline="") as file:

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        # Write the column headings
        writer.writeheader()

        # Write all expense records
        writer.writerows(expenses)


def load_expenses():
    """
    Reads existing expense records from the CSV file.
    """

    expenses = []

    # Check whether the CSV file exists
    if not os.path.exists(FILE_PATH):
        save_expenses(expenses)
        return expenses

    with open(FILE_PATH, mode="r", newline="") as file:

        reader = csv.DictReader(file)

        for row in reader:

            # Convert ID and Amount into numeric values
            row["ID"] = int(row["ID"])
            row["Amount"] = float(row["Amount"])

            expenses.append(row)

    return expenses