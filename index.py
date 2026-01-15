# Personal Expense Tracker (Simple Version)

expenses = []   # list to store expense records

def add_expense():
    name = input("Expense name: ")
    try:
        amount = float(input("Amount (₹): "))
    except ValueError:
        print("Invalid amount, please enter a number.")
        return
    category = input("Category: ")
    expenses.append({"name": name, "amount": amount, "category": category})
    print("Added:", name, "₹", amount, "under", category)

def view_expenses():
    if len(expenses) == 0:
        print("No expenses yet.")
        return
    print("\nExpenses:")
    for i, e in enumerate(expenses, 1):
        print(i, "-", e["name"], "₹", e["amount"], "(", e["category"], ")")

def total_expense():
    total = 0
    for e in expenses:
        total += e["amount"]
    print("Total spent: ₹", total)

def category_summary():
    if len(expenses) == 0:
        print("No expenses yet.")
        return
    summary = {}
    for e in expenses:
        if e["category"] in summary:
            summary[e["category"]] += e["amount"]
        else:
            summary[e["category"]] = e["amount"]
    print("\nCategory Summary:")
    for c in summary:
        print(c, "₹", summary[c])

# main loop
while True:
    print("\n--- Expense Tracker Menu ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Category Summary")
    print("5. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        total_expense()
    elif choice == "4":
        category_summary()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")
