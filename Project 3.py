import csv
from datetime import datetime

# Function to add an expense
def add_expense():
    date = input("Enter the date (YYYY-MM-DD): ")
    amount = input("Enter the amount spent: ")
    description = input("Enter a brief description: ")
    category = input("Enter the category (e.g., food, transportation, entertainment): ")

    try:
        amount = float(amount)
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")
        return

    expense = [date, amount, description, category]

    with open('expenses.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(expense)

    print("Expense added successfully!")

# Function to view expenses
def view_expenses():
    try:
        with open('expenses.csv', 'r') as file:
            reader = csv.reader(file)
            expenses = list(reader)

            if not expenses:
                print("No expenses recorded yet.")
                return

            for expense in expenses:
                print(expense)
    except FileNotFoundError:
        print("No expenses recorded yet.")

# Function to view summary
def view_summary():
    try:
        with open('expenses.csv', 'r') as file:
            reader = csv.reader(file)
            expenses = list(reader)

            if not expenses:
                print("No expenses recorded yet.")
                return

            total_expenses = 0
            category_expenses = {}

            for expense in expenses:
                date, amount, description, category = expense
                amount = float(amount)
                total_expenses += amount

                if category in category_expenses:
                    category_expenses[category] += amount
                else:
                    category_expenses[category] = amount

            print(f"Total Expenses: {total_expenses}")
            print("Category-wise Expenses:")
            for category, amount in category_expenses.items():
                print(f"{category}: {amount}")
    except FileNotFoundError:
        print("No expenses recorded yet.")

# Function to display the menu
def display_menu():
    print("1. Add an Expense")
    print("2. View Expenses")
    print("3. View Summary")
    print("4. Exit")

# Main function
def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            view_summary()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
