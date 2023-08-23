import csv
from datetime import datetime
from simple_term_menu import TerminalMenu
from prettycli import red
from sqlalchemy import func, extract

def retrieve_all(session, expense):
    return session.query(expense).order_by(expense.date).all()

def export_menu(expenses_list):
    export_options = ["Export", "Back"]
    export_menu = TerminalMenu(export_options, menu_highlight_style=("bg_black", "fg_cyan", "bold"), menu_cursor_style=("fg_blue",))
    export_index = export_menu.show()
    if export_options[export_index] == "Export":
        export(expenses_list)
    else:
        return
    
def export(expenses_list):
    header = ["ID", "Title", "Amount", "Date", "Category"]
    rows = []
    for expense in expenses_list:
        rows.append([
            expense.id,
            expense.title,
            expense.amount,
            expense.date,
            expense.category.name
        ])
    with open(f"../exports/expenses-{datetime.now().strftime('%m-%d_%H%M%S')}.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(rows)
    print("SUCCESSFULLY EXPORTED TO ../EXPORTS FOLDER")    

def filter_menu(results):
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
        return month_options[month_menu_index]
    
    elif filter_options[filter_menu_index] == "Category":
        category_options = ["Fun", "Bills", "Food", "Misc."]
        category_menu = TerminalMenu(category_options, title="SELECT CATEGORY:", menu_highlight_style=("bg_black", "fg_cyan", "bold"), menu_cursor_style=("fg_blue",))
        category_menu_index = category_menu.show()
        return category_menu_index + 1
    
def valid_date(date_string):
    try:
        datetime.strptime(date_string, "%m%d%y")
        return True
    except ValueError:
        return False
    
def validate_input():
    while True:
        date = input("DATE (MMDDYY): ")
        if date.isnumeric() and len(date) == 6 and valid_date(date):
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
    category_options = ["Fun", "Bills", "Food", "Misc."]
    category_menu = TerminalMenu(category_options, title="SELECT CATEGORY:", menu_highlight_style=("bg_black", "fg_cyan", "bold"), menu_cursor_style=("fg_blue",))
    category_menu_index = category_menu.show()
    
    return [title.capitalize(), amount, category_menu_index + 1, datetime.strptime(date, "%m%d%y")]

def view_all(session, expense):
    results = retrieve_all(session, expense)
    if results:
        expenses_options = [str(item) for item in results]
        expenses_menu = TerminalMenu(expenses_options, menu_highlight_style=("bg_black", "fg_cyan", "bold"), menu_cursor_style=("fg_blue",))
        expenses_menu_index = expenses_menu.show()
        print(f'SELECTED: {expenses_options[expenses_menu_index]}')

        edit_delete_options = ["Edit", "Delete", "Cancel"]
        edit_delete_menu = TerminalMenu(edit_delete_options, menu_highlight_style=("bg_black", "fg_cyan", "bold"), menu_cursor_style=("fg_blue",))
        edit_delete_menu_index = edit_delete_menu.show()
        if edit_delete_options[edit_delete_menu_index] == "Edit":
            edit(session, expense, results[expenses_menu_index].id)
        elif edit_delete_options[edit_delete_menu_index] == "Delete":
            delete(session, expense, results[expenses_menu_index].id)
        else:
            return
    else:
        print(red('NO EXPENSES FOUND'))
    
def add(session, expense):
    print('ADD EXPENSE: ')    
    values = validate_input()
    new_expense = expense(title=values[0], amount=values[1], category_id=values[2], date=values[3])
    session.add(new_expense)
    session.commit()
    print(f'\nEXPENSE ADDED: {new_expense}')

def edit(session, expense, id):
    selected_expense = session.query(expense).filter_by(id=id).first()
    values = validate_input()
    edited_expense = {
        "title":values[0],
        "amount":values[1],
        "category_id":values[2],
        "date":values[3]
    }
    for key, value in edited_expense.items():
        setattr(selected_expense, key, value)
    session.commit()
    print(f'\nEDITED: {selected_expense}')

def delete(session, expense, id):
    selected_expense = session.query(expense).filter_by(id=id).first()
    session.delete(selected_expense)
    session.commit()
    print('\nSUCCESSFULLY DELETED')

def filter(session, expense):
    results = retrieve_all(session, expense)
    if results:
        selection = filter_menu(results)
        if type(selection) is int:
            filtered_results = session.query(expense).filter(expense.category_id == selection).order_by(expense.date).all()
            for item in filtered_results:
                print(item)
            sum_by_category = session.query(func.sum(expense.amount)).filter(expense.category_id == selection).scalar()
            print(f"TOTAL: ${sum_by_category}.00")
            export_menu(filtered_results)

        elif type(selection) is str:
            filtered_results = session.query(expense).filter(extract('month', expense.date) == datetime.strptime(selection, "%B").month).order_by(expense.date).all()
            print(f"EXPENSES FOR MONTH OF: {selection}")
            for item in filtered_results:
                print(item)
            sum_by_month = session.query(func.sum(expense.amount)).filter(extract('month', expense.date) == datetime.strptime(selection, "%B").month).scalar()
            print(f"TOTAL: ${sum_by_month}.00")
            export_menu(filtered_results)
    else:
        print(red('NO EXPENSES FOUND'))
    

def custom_select(session, expense):
    results = retrieve_all(session, expense)
    if results:
        print("PRESS 'SPACE' TO SELECT ENTRIES, PRESS 'ENTER' TO CONTINUE WITH CURRENT SELECTION(S)")
        multi_select_options = [str(item) for item in results]
        multi_select_menu = TerminalMenu(multi_select_options, multi_select_empty_ok=True, multi_select=True, multi_select_select_on_accept=False, menu_highlight_style=("bg_black", "fg_cyan", "bold"), menu_cursor_style=("fg_blue",), multi_select_cursor_style=("fg_blue", "bold",), multi_select_cursor=("[x] "))
        selections = multi_select_menu.show()
        if selections:
            selected_expenses = [results[selection] for selection in selections]
            total_sum = 0
            print('\nSELECTED:')
            for expense in selected_expenses:
                print(expense)
                total_sum += expense.amount
            print(f"TOTAL: ${total_sum}.00")
            export_menu(selected_expenses)
        else: 
            print('NO EXPENSES SELECTED') 
    else:
        print(red('NO EXPENSES FOUND'))