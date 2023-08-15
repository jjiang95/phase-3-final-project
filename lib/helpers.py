from datetime import datetime
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
    category_options = ["Fun", "Bills", "Food", "Misc."]
    category_menu = TerminalMenu(category_options, title="SELECT CATEGORY:", menu_highlight_style=("bg_black", "fg_cyan", "bold"), menu_cursor_style=("fg_blue",))
    category_menu_index = category_menu.show()
    category_id = category_menu_index + 1
    
    return [title.capitalize(), amount, category_id, datetime.strptime(date, "%m%d%y")]

def view_all(session, expense):
    results = session.query(expense).order_by(expense.date).all()
    if results:
        expenses_options = [str(item) for item in results]
        expenses_menu = TerminalMenu(expenses_options, menu_highlight_style=("bg_black", "fg_cyan", "bold"), menu_cursor_style=("fg_blue",))
        expenses_menu_index = expenses_menu.show()
        print(f'SELECTED: {expenses_options[expenses_menu_index]}')
        options = ["Edit", "Delete", "Cancel"]
        edit_or_delete = TerminalMenu(options, menu_highlight_style=("bg_black", "fg_cyan", "bold"), menu_cursor_style=("fg_blue",))
        index = edit_or_delete.show()
        if options[index] == "Edit":
            edit(session, expense, results[expenses_menu_index].id)
        elif options[index] == "Delete":
            delete(session, expense, results[expenses_menu_index].id)
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
    results = session.query(expense).order_by(expense.date).all()
    if results:
        filter_options = ["Month", "Category", "Cancel"]
        filter_menu = TerminalMenu(filter_options, title="FILTER BY:", menu_highlight_style=("bg_black", "fg_cyan", "bold"), menu_cursor_style=("fg_blue",))
        filter_menu_index = filter_menu.show()
        if filter_options[filter_menu_index] == "Month":
            months_set = set()
            for result in results:
                months_set.add(result.date.strftime("%B"))
            month_options = sorted(list(months_set), key=lambda month: datetime.strptime(month, "%B"))
            month_menu = TerminalMenu(month_options, menu_highlight_style=("bg_black", "fg_cyan", "bold"), menu_cursor_style=("fg_blue",))
            month_menu_index = month_menu.show()
            filtered_results = [result for result in results if result.date.strftime("%B") == month_options[month_menu_index]]
            print(f"EXPENSES FOR MONTH OF: {month_options[month_menu_index]}")
            for item in filtered_results:
                print(item)
        elif filter_options[filter_menu_index] == "Category":
            category_options = ["Fun", "Bills", "Food", "Misc."]
            category_menu = TerminalMenu(category_options, title="SELECT CATEGORY:", menu_highlight_style=("bg_black", "fg_cyan", "bold"), menu_cursor_style=("fg_blue",))
            category_menu_index = category_menu.show()
            filtered_results = [result for result in results if result.category_id == category_menu_index + 1]
            print(f"EXPENSES IN CATEGORY: {category_options[category_menu_index]}")
            for item in filtered_results:
                print(item)
        elif filter_options[filter_menu_index] == "Cancel":
            return
    else:
        print(red('NO EXPENSES FOUND'))            
                 