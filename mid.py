# expense tracker project 

expenses = []  # list of expenses (each expense is a dictionary)

print("Welcome to Expense Tracker : kharcha kam kiya karo")

while True:
    print("\n======= MENU =======")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Total Expenses")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    # Add expense
    if choice == 1:
        date = input("Enter date (YYYY-MM-DD): ")
        category = input("Enter category (food / transport / entertainment): ")
        description = input("Enter description: ")
        amount = float(input("Enter amount: "))

        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }

        expenses.append(expense)
        print("✅ Expense added successfully!")

    # View all expenses
    elif choice == 2:
        if len(expenses) == 0:
            print("No expenses to show.")
        else:
            print("\n======= All Expenses =======")
            count = 1
            for expense in expenses:
                print(
                    f"{count}. Date: {expense['date']}, "
                    f"Category: {expense['category']}, "
                    f"Description: {expense['description']}, "
                    f"Amount: {expense['amount']}"
                )
                count += 1

    # View total expenses
    elif choice == 3:
        total = 0
        for expense in expenses:
            total += expense["amount"]
        print(f"💰 Total Expenses: {total}")

    # Exit
    elif choice == 4:
        print("Exiting the program...")
        break

    else:
        print("❌ Invalid choice, please try again.")
