#!/usr/bin/env python3

from models import Expense
from helpers import print_main_menu, option_1_view_all, option_2_add, option_3_edit, option_4_delete
from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('sqlite:///database.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    print('''
███████╗██╗░░██╗██████╗░███████╗███╗░░██╗░██████╗███████╗  ████████╗██████╗░░█████╗░░█████╗░██╗░░██╗███████╗██████╗░
██╔════╝╚██╗██╔╝██╔══██╗██╔════╝████╗░██║██╔════╝██╔════╝  ╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██║░██╔╝██╔════╝██╔══██╗
█████╗░░░╚███╔╝░██████╔╝█████╗░░██╔██╗██║╚█████╗░█████╗░░  ░░░██║░░░██████╔╝███████║██║░░╚═╝█████═╝░█████╗░░██████╔╝
██╔══╝░░░██╔██╗░██╔═══╝░██╔══╝░░██║╚████║░╚═══██╗██╔══╝░░  ░░░██║░░░██╔══██╗██╔══██║██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗
███████╗██╔╝╚██╗██║░░░░░███████╗██║░╚███║██████╔╝███████╗  ░░░██║░░░██║░░██║██║░░██║╚█████╔╝██║░╚██╗███████╗██║░░██║
╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚══════╝╚═╝░░╚══╝╚═════╝░╚══════╝  ░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
    ''')

    print_main_menu()
    # expense = session.query(Expense).filter_by(id=3).first()
    # expense.date = datetime(2023, 7, 25)
    # session.commit()
    # session.close()
    while True:
        menu_option = input("\nSELECT MENU OPTION: ")
        if menu_option.isdigit() and menu_option > '0' and menu_option < '8':
            if menu_option == '1':
                print('ALL EXPENSES: ')
                option_1_view_all(session, Expense)
            elif menu_option == '2':
                option_2_add(session, Expense)
            elif menu_option == '3':
                option_3_edit(session, Expense)
            elif menu_option == '4':
                option_4_delete(session, Expense)
            elif menu_option == '5':
                pass
            elif menu_option == '6':
                pass
            else:
                print('GOODBYE!')
                break
        else:
            print('PLEASE ENTER VALID MENU OPTION')
    

    # import ipdb; ipdb.set_trace()