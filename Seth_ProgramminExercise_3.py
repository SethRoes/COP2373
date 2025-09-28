# The code is calculating different monthly expenses and displaying the total, with the highest and lowest.
from functools import reduce

def get_expenses():

    # Displays the text
    expenses = []
    while True:
        expense_type = input("Enter expense type (or 'done' to finish): ").strip()
        if expense_type.lower() == 'done':
            break
        while True:
            try:
                amount = float(input(f"Enter amount for {expense_type}: "))
                if amount < 0:
                    print("Amount cannot be negative. Please enter a positive number.")
                else:
                    expenses.append({'type': expense_type, 'amount': amount})
                    break
            except ValueError:
                print("Invalid amount. Please enter a number.")
    return expenses

def analyze_expenses(expenses):
    if not expenses:
        return 0, None, None

    # Calculate total expenses.
    total_expense = reduce(lambda acc, expense: acc + expense['amount'], expenses, 0)

    highest_expense_item = reduce(lambda acc, expense: expense if expense['amount'] > acc['amount'] else acc, expenses)

    lowest_expense_item = reduce(lambda acc, expense: expense if expense['amount'] < acc['amount'] else acc, expenses)

    return total_expense, highest_expense_item, lowest_expense_item

if __name__ == "__main__":
    monthly_expenses = get_expenses()

    if monthly_expenses:
        total, highest, lowest = analyze_expenses(monthly_expenses)

        print("\n--- Expense Summary ---")
        print(f"Total Monthly Expense: ${total:.2f}")
        print(f"Highest Expense: {highest['type']} - ${highest['amount']:.2f}")
        print(f"Lowest Expense: {lowest['type']} - ${lowest['amount']:.2f}")
    else:
        print("No expenses entered.")