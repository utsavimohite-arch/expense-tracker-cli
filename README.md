# Expense Tracker Application

A simple command-line Expense Tracker built using Python. It allows users to record, view, search, calculate, summarize, and delete their expenses. Expense records are stored permanently in a CSV file.

## Project Information

| Detail | Description |
|---|---|
| Project Name | Expense Tracker Application |
| Organization | CodeOrbit Tech |
| Programming Language | Python |
| Application Type | Command-Line Interface (CLI) |
| Storage | CSV File |
| Version | 1.0.0 |

## Features

1. **Add Expense:** Record a new expense with its category, description, and amount. The application automatically generates an ID and records the current date.
2. **View All Expenses:** Display all saved expense records.
3. **Search Expenses by Category:** Find expenses belonging to a particular category.
4. **Calculate Total Expenses:** Calculate the total amount spent across all recorded expenses.
5. **Category-wise Expense Summary:** Display spending grouped by category.
6. **Delete an Expense:** Delete an expense using its unique ID, with confirmation before deletion.
7. **CSV Data Storage:** Save expenses in a CSV file so that records remain available after restarting the application.
8. **Input Validation:** Handle invalid amounts, empty fields, and incorrect menu inputs.
9. **Error Handling:** Handle common CSV file reading and writing errors.

## Technologies Used

- **Python:** Core programming language.
- **CSV Module:** Stores and retrieves expense records.
- **OS Module:** Handles file paths and file existence.
- **Math Module:** Validates numeric expense amounts.
- **Git and GitHub:** Version control and project hosting.

## Project Structure

```text
expense-tracker-cli/
│
├── main.py              # Main application and menu
├── expense_manager.py   # Expense management operations
├── csv_handler.py       # CSV reading and writing
├── expenses.csv         # Stores expense records
├── README.md            # Project documentation
├── CHANGELOG.md         # Project version history
└── .gitignore           # Files excluded from Git
```

## Requirements

- Python 3.8 or above
- Git
- A code editor such as Visual Studio Code

No external Python packages are required.

## Installation and Setup

### 1. Clone the Repository

Open your terminal and run:

```bash
git clone https://github.com/utsavimohite-arch/expense-tracker-cli.git
```

### 2. Navigate to the Project Folder

```bash
cd expense-tracker-cli
```

### 3. Run the Application

```bash
python main.py
```

On some systems, you may need to use:

```bash
python3 main.py
```

## Application Menu

When you run the application, the following menu is displayed:

```text
===== EXPENSE TRACKER =====

1. Add Expense
2. View All Expenses
3. Search Expenses by Category
4. Calculate Total Expenses
5. Category-wise Expense Summary
6. Delete an Expense
7. Exit

Enter your choice:
```

Select an option by entering its corresponding number.

## Data Storage

All expense records are stored in `expenses