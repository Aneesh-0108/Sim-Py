from datetime import datetime
from storage import load_expenses, save_expenses
from model import Expense

def add_expense(title, amount_num, category):
    try:
        amount = float(amount_num)
        if amount <= 0:
            return f"The amount entered must be greater than 0"
    except ValueError:
        return f"The amount must be valid"

    new_expense = Expense(title=title, amount_num=amount, category=category)
    
    current_expenses = load_expenses()
    # append and convert the dataclassinto a dictionary before appending
    current_expenses.append(new_expense.to_dict())
    save_expenses(current_expenses)

    return f"Success: Added '{title}' to the Expense"

def view_expense():
    # capture the data
    data = load_expenses()
    if not data:
        return ["No expenses found"]
     
    formatted_expenses = []
    for expense in data:
        line = f"[{expense['date']}] {expense['title']} - ${expense['amount']:.2f} ({expense['category']})"
        formatted_expenses.append(line)
           
    return formatted_expenses

def delete_expense(title: str):
    expenses = load_expenses()

    if not expenses:
        return ["Error: No expenses recorded yet"]
     
    initial_count = len(expenses)

    # List comprehension (Fixed!)
    updated_expenses = [
        expense for expense in expenses
        if expense['title'].lower() != title.strip().lower()
    ]

    if len(updated_expenses) == initial_count:
        # Added missing 'f' prefix
        return [f"No Expense found with the title '{title}'"]

    save_expenses(updated_expenses)
    deleted_count = initial_count - len(updated_expenses)

    # Added missing 'f' prefix and closing single quote
    return [f"Success: Deleted {deleted_count} expense(s) matching '{title}'"]

def search_expense(title: str):
    expenses = load_expenses()

    if not expenses:
        return "No Expenses recorded yet!"  # Changed to string to match single-item display
     
    for expense in expenses:
        if expense['title'].lower() == title.strip().lower():
            # Added missing dot before 2f
            return f"[{expense['date']}] {expense['title']} - ${expense['amount']:.2f} ({expense['category']})"
          
    return f"No expense found matching '{title}'"     

def calculate_total():
    expenses = load_expenses()
    total = 0.0

    for expense in expenses:
        # Fixed 'tot' typo to 'total'
        total += float(expense['amount'])

    # Added missing dot before 2f
    return f"Total Expenses: ${total:.2f}"     

def filter_by_category(category: str):
    expenses = load_expenses()

    if not expenses:
        return ["No Expenses recorded yet!"]

    filtered_lines = []

    for expense in expenses:
        if expense['category'].lower() == category.strip().lower():
            line = f"[{expense['date']}] {expense['title']} - ${expense['amount']:.2f}"
            filtered_lines.append(line)

    if not filtered_lines:
        return [f"No expenses found in the category '{category}'."]

    return filtered_lines