from datetime import datetime
from sqlalchemy import extract
from simple_term_menu import TerminalMenu
from prettycli import red

def print_main_menu():
    print('''ENTER OPTION NUMBER AND PRESS 'ENTER'              
1. View all
2. Add
3. Edit
4. Delete
5. Filter
6. Aggregate
7. Exit''')

def validate_input():
    title = input("TITLE: ")
    while True:
        amount = input("AMOUNT: ")
        if amount.isnumeric():
            break
        else:
            print(red('PLEASE ENTER A WHOLE NUMBER (ROUNDED UP)'))
    while True:    
        category_id = input("CHOOSE CATEGORY: 1. Fun 2. Bills 3. Food 4. Misc.\n")
        if category_id.isdigit() and '1' <= category_id <= '4':
            break
        else:
            print(red('PLEASE ENTER VALID OPTION'))
    
    return [title, amount, category_id]

def option_1_view_all(session, expense):
    results = session.query(expense).all()
    menu_list = [str(item) for item in results]
    expenses_menu = TerminalMenu(menu_list)
    menu_entry_index = expenses_menu.show()
    # if results:
    #     for result in results:
    #         print(result)
    # else:
    #     print('none')
    
def option_2_add(session, expense):
    print('ADD EXPENSE: ')    
    values = validate_input()
    expense = expense(title=values[0], amount=values[1], category_id=values[2], date=datetime.now())
    session.add(expense)
    session.commit()
    print('EXPENSE ADDED')

def option_3_edit(session, expense):
    print('SELECT EXPENSE TO EDIT: ')
    option_1_view_all(session, expense)
    while True:
        id = input('EXPENSE ID: ')
        selected_expense = session.query(expense).filter_by(id=id).first()
        if selected_expense:
            values = validate_input()
            selected_expense.title = values[0]
            selected_expense.amount = values[1]
            selected_expense.category_id = values[2]
            session.commit()
            print(f'\nEDITED:\n{selected_expense}')
            break
        else:
            print(red('INVALID ID'))

def option_4_delete(session, expense):
    print('SELECT EXPENSE TO DELETE: ')
    option_1_view_all(session, expense)
    while True:
        id = input('EXPENSE ID: ')
        selected_expense = session.query(expense).filter_by(id=id).first()
        if selected_expense:
            session.delete(selected_expense)
            session.commit()
            print(f'\nSUCCESSFULLY DELETED')
            break
        else:
            print(red('INVALID ID'))

def option_5_filter(session, expense):
    print('FILTER BY: 1. Month 2. Category')
    while True:
        filter = input('SELECT: ')
        if filter.isdigit() and '1' <= filter <= '2':
            break
        else:
            print(red('PLEASE ENTER VALID OPTION'))
    if filter == '1':
        while True:
            month = input('ENTER MONTH (MM): ')
            if month.isdigit() and len(month) == 2:
                month_int = int(month)
                results = session.query(expense).filter(extract('month', expense.date) == month_int).all()
                if results:
                    for result in results:
                        print(result)
                    break
                else: 
                    print(f'NO RESULTS FOR MONTH: {month}')
                    break
            else:
                print("PLEASE ENTER MONTH IN MM NUMERIC FORMAT")
    elif filter == '2':
        while True:
            category = input('SELECT CATEGORY: 1. Fun 2. Bills 3. Food 4. Misc.: ')
            if category.isdigit() and '1' <= category <= '4':
                results = session.query(expense).filter_by(category_id=category).all()
                for result in results:
                    print(result)
                break
            else:
                print(red('PLEASE ENTER VALID OPTION'))
            
                 