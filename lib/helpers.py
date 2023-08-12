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

def option_2(session, expense, category):
    print('ADD EXPENSE')
    title = input("TITLE: ")
    amount = input("AMOUNT: ")
    category_id = input("CHOOSE CATEGORY: 1. Fun 2. Bills 3. Food 4. Misc.\n")
    
    category = session.query(category).filter_by(id=category_id).first()
    expense = expense(title=title, amount=amount, category=category, date=datetime.now())
    session.add(expense)
    session.commit()
    print('EXPENSE ADDED')

