from datetime import datetime
from sqlalchemy import extract, func
from simple_term_menu import TerminalMenu
from prettycli import red

def validate_input():
    while True:
        date = input("DATE (MMDDYY): ")
        if date.isnumeric() and len(date) == 6:
            break
        else:
            print(red('PLEASE ENTER DATE IN PROPER FORMAT (MMDDYY)'))
    title = input("TITLE: ")
    while True:
        amount = input("AMOUNT: ")
        if amount.isnumeric():
            break
        else:
            print(red('PLEASE ENTER A WHOLE NUMBER (ROUNDED UP)'))
    category_id = 0
    categories = ["Fun", "Bills", "Food", "Misc."]
    category_menu = TerminalMenu(categories, title="SELECT CATEGORY:", menu_highlight_style=("bg_black", "fg_cyan"), menu_cursor_style=("fg_blue",))
    menu_entry_index = category_menu.show()
    category_id = menu_entry_index + 1
    
    return [title.capitalize(), amount, category_id, datetime.strptime(date, "%m%d%y")]

def view_all(session, expense):
    results = session.query(expense).all()
    if results:
        menu_list = [str(item) for item in results]
        expenses_menu = TerminalMenu(menu_list, menu_highlight_style=("bg_black", "fg_cyan"), menu_cursor_style=("fg_blue",))
        menu_entry_index = expenses_menu.show()
        print(f'SELECTED: {menu_list[menu_entry_index]}')
        options = ["Edit", "Delete", "Cancel"]
        edit_or_delete = TerminalMenu(options, menu_highlight_style=("bg_black", "fg_cyan"), menu_cursor_style=("fg_blue",))
        index = edit_or_delete.show()
        if options[index] == "Edit":
            edit(session, expense, results[menu_entry_index].id)
        elif options[index] == "Delete":
            delete(session, expense, results[menu_entry_index].id)
        elif options[index] == "Cancel":
            return
    else:
        print(red('NO EXPENSES FOUND'))
    
def add(session, expense):
    print('ADD EXPENSE: ')    
    values = validate_input()
    expense = expense(title=values[0], amount=values[1], category_id=values[2], date=values[3])
    session.add(expense)
    session.commit()
    print('\nEXPENSE ADDED')

def edit(session, expense, id):
    selected_expense = session.query(expense).filter_by(id=id).first()
    values = validate_input()
    selected_expense.title = values[0]
    selected_expense.amount = values[1]
    selected_expense.category_id = values[2]
    selected_expense.date = values[3]
    session.commit()
    print(f'\nEDITED: {selected_expense}')

def delete(session, expense, id):
    selected_expense = session.query(expense).filter_by(id=id).first()
    session.delete(selected_expense)
    session.commit()
    print('\nSUCCESSFULLY DELETED')

def filter(session, expense):
    month_or_category = ["Month", "Category", "Cancel"]
    filter_menu = TerminalMenu(month_or_category, title="FILTER BY:", menu_highlight_style=("bg_black", "fg_cyan"), menu_cursor_style=("fg_blue",))
    index = filter_menu.show()
    if month_or_category[index] == "Month":
        results = session.query(expense).all()
        months_set = set()
        for result in results:
            months_set.add(result.date.strftime("%B"))
        month_options = list(months_set)
        months_menu = TerminalMenu(month_options, menu_highlight_style=("bg_black", "fg_cyan"), menu_cursor_style=("fg_blue",))
        month_index = months_menu.show()
        filtered_results = [result for result in results if result.date.strftime("%B") == month_options[month_index]]
        print(f"EXPENSES FOR MONTH OF: {month_options[month_index]}")
        for filtered_result in filtered_results:
            print(filtered_result)
    elif month_or_category[index] == "Category":
        pass
    elif month_or_category[index] == "Cancel":
        return

    # elif filter == '2':
    #     while True:
    #         category = input('SELECT CATEGORY: 1. Fun 2. Bills 3. Food 4. Misc.: ')
    #         if category.isdigit() and '1' <= category <= '4':
    #             results = session.query(expense).filter_by(category_id=category).all()
    #             for result in results:
    #                 print(result)
    #             break
    #         else:
    #             print(red('PLEASE ENTER VALID OPTION'))
            
                 