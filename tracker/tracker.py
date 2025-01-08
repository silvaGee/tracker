import csv

def add_expense():
  """Prompts the user for expense details and adds it to the expense list."""
  date = input("Enter the date of the expense (YYYY-MM-DD): ")
  category = input("Enter the category of the expense: ")
  amount = float(input("Enter the amount spent: "))
  description = input("Enter a brief description of the expense: ")
  expense = {'date': date, 'category': category, 'amount': amount, 'description': description}
  expenses.append(expense)
  print("Expense added successfully!")

def view_expenses():
  """Displays all stored expenses."""
  if not expenses:
    print("No expenses found.")
    return

  print("Expenses:")
  for expense in expenses:
    print(f"Date: {expense['date']}")
    print(f"Category: {expense['category']}")
    print(f"Amount: ${expense['amount']:.2f}")
    print(f"Description: {expense['description']}")
    print("-" * 20)

def track_budget():
  """Calculates and displays the remaining budget."""
  global monthly_budget
  if monthly_budget is None:
    monthly_budget = float(input("Enter your monthly budget: "))

  total_expenses = sum(expense['amount'] for expense in expenses)
  remaining_budget = monthly_budget - total_expenses

  if remaining_budget < 0:
    print("You have exceeded your budget!")
  else:
    print(f"You have ${remaining_budget:.2f} left for the month.")

def save_expenses():
  """Saves expenses to a CSV file."""
  with open('expenses.csv', 'w', newline='') as file:
    fieldnames = ['date', 'category', 'amount', 'description']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(expenses)
  print("Expenses saved to expenses.csv")

def load_expenses():
  """Loads expenses from a CSV file."""
  try:
    with open('expenses.csv', 'r') as file:
      reader = csv.DictReader(file)
      global expenses
      expenses = [row for row in reader]
  except FileNotFoundError:
    print("No expense data found.")

def main_menu():
  """Displays the main menu and handles user input."""
  while True:
    print("\nExpense Tracker Menu")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Track Budget")
    print("4. Save Expenses")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
      add_expense()
    elif choice == '2':
      view_expenses()
    elif choice == '3':
      track_budget()
    elif choice == '4':
      save_expenses()
    elif choice == '5':
      save_expenses()
      print("Exiting...")
      break
    else:
      print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
  expenses = []
  monthly_budget = None
  load_expenses()
  main_menu()
