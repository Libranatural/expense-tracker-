# expense tracker project 

expenses = []  # list of expenses in form of dictionary

print("welcome to expense tracker : khrcha kam kiya karo")

while True:
    print("=======MENU=======")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. view Total Expenses")
    print("4. exit")

    choice = int(input("enter your choice :"))

    # add expenses 
    if choice == 1:
            date = input("enter date (YYYY-MM-DD): ")
            category = input("enter category (e.g., food , transport  , entertainment ): ")
            description = input("enter description : ")
            amount = float(input("enter amount : "))
            expenses ={
                  "date": date,
                  "category": category,
                  "description": description,
                  "amount": amount
            }

            expenses.append(expenses)
            print("expense added successful:")

 # view all expenses
    elif choice == 2:
        if len(expenses) == 0:
            print("no expenses to show")
        else:
            print("======= all expenses =======")
            count = 1
            for expense in expenses:
                print(f"expenses {count} ->: date: {expense['date']}, category: {expense['category']}, description: {expense['description']}, amount: {expense['amount']}")
                count += 1

    # view total expenses
    elif choice == 3:
        total = 0
        for expense in expenses:
            total += expense['amount']
        print(f"total expenses: {total}")

    # exit
    elif choice == 4:
        print("Exiting the program...")
        break

    else:
        print("invalid choice, please try again,")