#!/usr/bin/env python3

from models import Expense
from helpers import view_all, add, filter
from datetime import datetime

from simple_term_menu import TerminalMenu
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def main():
    print('''
███████╗██╗░░██╗██████╗░███████╗███╗░░██╗░██████╗███████╗  ████████╗██████╗░░█████╗░░█████╗░██╗░░██╗███████╗██████╗░
██╔════╝╚██╗██╔╝██╔══██╗██╔════╝████╗░██║██╔════╝██╔════╝  ╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██║░██╔╝██╔════╝██╔══██╗
█████╗░░░╚███╔╝░██████╔╝█████╗░░██╔██╗██║╚█████╗░█████╗░░  ░░░██║░░░██████╔╝███████║██║░░╚═╝█████═╝░█████╗░░██████╔╝
██╔══╝░░░██╔██╗░██╔═══╝░██╔══╝░░██║╚████║░╚═══██╗██╔══╝░░  ░░░██║░░░██╔══██╗██╔══██║██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗
███████╗██╔╝╚██╗██║░░░░░███████╗██║░╚███║██████╔╝███████╗  ░░░██║░░░██║░░██║██║░░██║╚█████╔╝██║░╚██╗███████╗██║░░██║
╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚══════╝╚═╝░░╚══╝╚═════╝░╚══════╝  ░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
    ''')
    options = ["View all", "Add", "Filter", "Aggregate", "Exit"]
    main_menu = TerminalMenu(options)
    while True:
        print()
        menu_entry_index = main_menu.show()
        if options[menu_entry_index] == "View all":
            view_all(session, Expense)
        elif options[menu_entry_index] == "Add":
            add(session, Expense)
        elif options[menu_entry_index] == "Filter":
            filter(session, Expense)
        elif options[menu_entry_index] == "Aggregate":
            pass
        elif options[menu_entry_index] == "Exit":
            print('EXITING...')
            break   

if __name__ == '__main__':
    engine = create_engine('sqlite:///database.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    main()
    # print_main_menu()
    # # expense = session.query(Expense).filter_by(id=3).first()
    # # expense.date = datetime(2023, 7, 25)
    # # session.commit()
    # # session.close()
    # while True:
    #     menu_option = input("\nSELECT MENU OPTION: ")
    #     if menu_option.isdigit() and menu_option > '0' and menu_option < '8':
    #         if menu_option == '1':
    #             print('ALL EXPENSES: ')
    #             option_1_view_all(session, Expense)
    #         elif menu_option == '2':
    #             option_2_add(session, Expense)
    #         elif menu_option == '3':
    #             option_3_edit(session, Expense)
    #         elif menu_option == '4':
    #             option_4_delete(session, Expense)
    #         elif menu_option == '5':
    #             option_5_filter(session, Expense)
    #         elif menu_option == '6':
    #             pass
    #         else:
    #             print('GOODBYE!')
    #             break
    #     else:
    #         print('PLEASE ENTER VALID MENU OPTION')
    
    # import ipdb; ipdb.set_trace()