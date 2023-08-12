#!/usr/bin/env python3

from models import Expense, Category
from helpers import print_main_menu, option_1, option_2

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
    while True:
        menu_option = input("SELECT MENU OPTION: ")
        if menu_option.isdigit() and menu_option > '0' and menu_option < '8':
            if menu_option == '1':
                option_1(session, Expense)
            elif menu_option == '2':
                option_2(session, Expense)
            elif menu_option == '3':
                pass
            elif menu_option == '4':
                pass
            elif menu_option == '5':
                pass
            elif menu_option == '6':
                pass
            else:
                print('Goodbye!')
                break
        else:
            print('PLEASE ENTER VALID MENU OPTION')
    
    # expense = session.query(Expense).filter_by(id=5).first()
    # expense.category_id = 4
    # session.commit()
    session.close()

    # import ipdb; ipdb.set_trace()