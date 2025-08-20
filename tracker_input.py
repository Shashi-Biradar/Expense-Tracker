from auth import init_user_table, register, login

from expenses import init_expense_table, insert_expense, view_all_expenses, search_by_category,delete_expense,updated_expense
import csv 

def run_tracker(user_id):
    while True:
        print("\n 1. Add new expense")
        print("\n 2. View all expenses")
        print("\n 3. Search by category")
        print("\n 4. Update expense")
        print("\n 5. Delete expense")
        print("\n 6. Export to CSV")
        print("\n 7. Logout ")

        choice = input('Choose an option: ')

        if choice == '1':
            amount = input('Amount: ')
            category = input('Category: ')
            description = input('Description: ')
            date = input('Date: ')

            insert_expense(user_id, amount, category, description, date)

        elif choice == '2':
            expenses = view_all_expenses(user_id)
            if expenses: 
                print("\n")
                print('List of Expenses: ')
                print('--------------------------------------')
                for expense in expenses:
                    print(f" {expense[2]} - {expense[3]} - {expense[4]} - {expense[5]}")
            else:
                print('No expenses found')

        elif choice == '3':
            category = input('Category: ')
            expenses = search_by_category(user_id, category)
            if expenses: 
                print("\n")
                print('List of Expenses: ')
                print('--------------------------------------')
                for expense in expenses:
                    print(f" {expense[2]} - {expense[3]} - {expense[4]} - {expense[5]}")
            else:
                print('No expenses found')
        
        elif choice == '4':
            print('Future enhancement - Update Expense')
            id = input('Enter Expense ID to update: ')
            rows_updated = updated_expense(id)
            if rows_updated:
                print('Expense updated successfully.')
            else:
                print('No expense found with that ID.')
                
        
        elif choice == '5':
            print('Future enhancement - Delete Expense')
            id = input('Enter Expense ID to delete: ')
            rows_deleted = delete_expense(id)
            if rows_deleted:
                print('Expense deleted successfully.')
            else:
                print('No expense found with that ID.')

        elif choice == '6':
            expenses = view_all_expenses(user_id)

            with open('expenses.csv', 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['Id', 'User Id', 'Amount', 'Category', 'Description', 'Date'])
                
                for row in expenses:
                    writer.writerow(row)

                print('Exported data into csv successfully')

        elif choice == '7':
            exit()

def login_user():
    print('Welcome to Expense Tracker')
    while True:
        print(" 1. Login")
        print("\n 2. Register")
        print("\n 3. Exit")

        choice = input('Choose an option: ')

        if choice == '1':
            username = input('Username: ')
            password = input('Password: ')

            user_id = login(username, password)

            if (user_id):
                print(f'Logged in as {username}')
                return user_id
            else:
                print('Invalid username or password')

        elif choice == '2':
            name = input('Name: ')
            email = input('Email: ')
            username = input('Username: ')
            password = input('Password: ')

            register(name, email, username, password)

        elif choice == '3':
            exit()


init_user_table()
init_expense_table()

user_id = login_user()
run_tracker(user_id)