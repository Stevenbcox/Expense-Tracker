import csv
import os
from datetime import datetime

FILENAME = r"P:\Users\Steven Cox\Book1.csv"

def add_expense():
    date = datetime.now().strftime('%Y-%m-%d')
    category = input("Category (ex. food, transport, bills): ").strip()
    description = input("Description: ").strip()
    amount = input("Amount: ").strip()

    with open(FILENAME, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, description, amount])
    print("✅ Expense added!")

def view_expenses():
    if not os.path.exists(FILENAME):
        print("No Expenses Found.")
        return

    with open(FILENAME, 'r') as file:
        reader = csv.reader(file)
        print("\nDate       | Category      | Description       | Amount        ")
        print("-" * 60)
        next(reader)
        for row in reader:
            print(f"{row[0]:10} | {row[1]:12} | {row[2]:20} | {row[3]}")

def main():
    while True:
        print("\n=== Expense Tracker ===")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")

        choice = input("Choose an Option: ").strip()
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            print("Goodbye.")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()