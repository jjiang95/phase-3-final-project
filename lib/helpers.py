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

