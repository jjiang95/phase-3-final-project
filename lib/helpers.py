from datetime import datetime
from sqlalchemy import extract
from simple_term_menu import TerminalMenu
from prettycli import red

def validate_input():
    title = input("TITLE: ")
    while True:
        amount = input("AMOUNT: ")
        if amount.isnumeric():
            break
        else:
            print(red('PLEASE ENTER A WHOLE NUMBER (ROUNDED UP)'))
    category_id = 0
    categories = ["Fun", "Bills", "Food", "Misc."]
    category_menu = TerminalMenu(categories)
    print("SELECT CATEGORY")
    menu_entry_index = category_menu.show()
    if categories[menu_entry_index] == categories[menu_entry_index]:
        category_id = menu_entry_index + 1
    # while True:    
    #     category_id = input("CHOOSE CATEGORY: 1. Fun 2. Bills 3. Food 4. Misc.\n")
    #     if category_id.isdigit() and '1' <= category_id <= '4':
    #         break
    #     else:
    #         print(red('PLEASE ENTER VALID OPTION'))
    
    return [title, amount, category_id]

def view_all(session, expense):
    results = session.query(expense).all()
    if results:
        menu_list = [str(item) for item in results]
        expenses_menu = TerminalMenu(menu_list)
        menu_entry_index = expenses_menu.show()
        if menu_list[menu_entry_index] == menu_list[menu_entry_index]:
            print(f'SELECTED: {menu_list[menu_entry_index]}')
            options = ["Edit", "Delete", "Cancel"]
            edit_or_delete = TerminalMenu(options)
            index = edit_or_delete.show()
            if options[index] == "Edit":
                edit(session, expense, results[menu_entry_index].id)
                return
            elif options[index] == "Delete":
                delete(session, expense, results[menu_entry_index].id)
                return
            elif options[index] == "Cancel":
                return
    else:
        print('NO EXPENSES FOUND')
    
def add(session, expense):
    print('ADD EXPENSE: ')    
    values = validate_input()
    expense = expense(title=values[0], amount=values[1], category_id=values[2], date=datetime.now())
    session.add(expense)
    session.commit()
    print('EXPENSE ADDED')

def edit(session, expense, id):
    selected_expense = session.query(expense).filter_by(id=id).first()
    values = validate_input()
    selected_expense.title = values[0]
    selected_expense.amount = values[1]
    selected_expense.category_id = values[2]
    session.commit()
    print(f'\nEDITED:\n{selected_expense}')

def delete(session, expense, id):
    selected_expense = session.query(expense).filter_by(id=id).first()
    session.delete(selected_expense)
    session.commit()
    print(f'\nSUCCESSFULLY DELETED')

def filter(session, expense):
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
            
                 