from functools import reduce

def get_expenses():

    """
    Asks the user to enter expense types and amounts.
    Returns a dictionary containing expense data.
    """

    expenses = []

    while True:
        expense_type = input("Enter expense type (or 'done' to finish): ")

        if expense_type.lower() == 'done':
            break

        try:
            amount = float(input("Enter amount for {}: ".format(expense_type)))
            expenses.append({"type": expense_type, "amount": amount})

        except ValueError:
            print("Invalid amount. Please enter a numeric value.")

    return expenses

def calculate_total(expenses):
    """
    Uses reduce to calculate the total amount expenses.
    Returns the total amount expenses.
    """
    return reduce(lambda total, expense: total + expense["amount"], expenses, 0)

def find_highest(expenses):
    """
    Uses reduce to find the highest amount expenses.
    Returns the highest amount expenses.
    """
    return reduce(lambda x, y: x if x["amount"] > y["amount"] else y, expenses)

def find_lowest(expenses):
    """
    Uses reduce to find the lowest amount expenses.
    Returns the lowest amount expenses.
    """
    return reduce(lambda x, y: x if x["amount"] < y["amount"] else y, expenses)

def main():
    expenses = get_expenses()

    if not expenses:
        print("No expenses found.")
        return

    total = calculate_total(expenses)
    highest = find_highest(expenses)
    lowest = find_lowest(expenses)

    print("\n---- Expense Summary ----")
    print("Total Expenses: ${:.2f}".format(total))
    print("Highest Expenses: {} - ${:.2f}".format(highest["type"], highest["amount"]))
    print("Lowest Expenses: {} - ${:.2f}".format(lowest["type"], lowest["amount"]))

if __name__ == '__main__':
    main()


