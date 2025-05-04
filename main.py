expenses = []

def print_expenses():
    print(expenses)

def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    
    try:
        amount = float(input("Enter amount in ₹: "))
    except:
        print("❌ Invalid amount. Please enter a number.")
        return
    
    category = input("Enter category (e.g., Food, Travel, Bills): ")
    note = input("Enter a note or description: ")

    expense = {
        "date"  : date,
        "amount" : amount,
        "category" : category,
        "note" : note
    }
    

    expenses.append(expense)
    print("✅ Expense added successfully.")

def list_expenses():
    if len(expenses) == 0:
        print("❌ No expenses to show.")
        return
    
    print("\n--- Expenses ---")
    for exp in expenses:
        print(f"Date: {exp['date']}, Category: {exp['category']}, Amount: ₹{exp['amount']}, Note: {exp['note']}")
    print("----------------")


def main():
    while True:
        print("\nExpense Tracker Menu")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        choice = int(input("Choose an option : "))

        if choice == 1:
            add_expense()
        elif choice  == 2:
            list_expenses()
        elif choice == 3:
            print("👋 Exiting the program. Bye!")
            break
        elif choice == 99:
            print_expenses()
        else:
            print("❌ Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()