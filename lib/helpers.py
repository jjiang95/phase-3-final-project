from datetime import datetime

def print_main_menu():
    print('''Enter option number and press 'enter'              
1. View all
2. Add
3. Edit
4. Delete
5. Filter
6. Export
7. Exit''')

def validate_input():
    title = input("TITLE: ")
    while True:
        amount = input("AMOUNT: ")
        if amount.isnumeric():
            break
        else:
            print('PLEASE ENTER A WHOLE NUMBER (ROUNDED UP)')
    while True:    
        category_id = input("CHOOSE CATEGORY: 1. Fun 2. Bills 3. Food 4. Misc.\n")
        if category_id.isdigit() and '1' <= category_id <= '4':
            break
        else:
            print('PLEASE ENTER VALID OPTION')
    
    return [title, amount, category_id]

def option_1(session, expense):
    results = session.query(expense).all()
    for result in results:
        print(result)
    
def option_2(session, expense):
    values = validate_input()
    expense = expense(title=values[0], amount=values[1], category_id=values[2], date=datetime.now())
    session.add(expense)
    session.commit()

def option_3(session, expense):
    print('SELECT EXPENSE TO EDIT')
    option_1(session, expense)
    while True:
        id = input('EXPENSE ID: ')
        selected_expense = session.query(expense).filter_by(id=id).first()
        if selected_expense:
            values = validate_input()
            selected_expense.title = values[0]
            selected_expense.amount = values[1]
            selected_expense.category_id = values[2]
            session.commit()
            print(f'EXPENSE EDITED\n{selected_expense}')
            break
        else:
            print('INVALID ID')
