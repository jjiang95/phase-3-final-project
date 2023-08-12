from datetime import datetime

def print_main_menu():
    print('''
Enter option number and press 'enter'              
1. View all
2. Add
3. Edit
4. Delete
5. Filter
6. Export
7. Exit
    ''')

def option_1(session, expense):
    print('ALL EXPENSES')
    results = session.query(expense).all()
    for result in results:
        print(result)

def option_2(session, expense):
    print('ADD EXPENSE')
    title = input("TITLE: ")
    while True:
        amount = input("AMOUNT: ")
        if amount.isnumeric():
            break
        else:
            print('PLEASE ENTER A WHOLE NUMBER')
    while True:    
        category_id = input("CHOOSE CATEGORY: 1. Fun 2. Bills 3. Food 4. Misc.\n")
        if category_id.isdigit() and '1' <= category_id <= '4':
            break
        else:
            print('PLEASE ENTER VALID OPTION')
    
    expense = expense(title=title, amount=amount, category_id=category_id, date=datetime.now())
    session.add(expense)
    session.commit()
    print('EXPENSE ADDED\n')

