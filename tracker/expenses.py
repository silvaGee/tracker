import csv

def add_expense():
     date = input("Please input the date of the expense in the format YYYY-MM-DD")
     category = input("Please input the category of the expense, for example Food or Travel")
     amount = float(input("Please input the amount spent"))
     description = input("Please input a brief description")
     expense = {"date": date, "category":category, "amount":amount, "description": description}
     expenses.append(expense)

def view_expense():
     for expense in expenses:
          if not all(key in expense for key in ["date", "category", "amount", "description"]):
               print("Incomplete expense")
               continue
          print(expense)

if __name__ == "__main__":
     expenses = []
