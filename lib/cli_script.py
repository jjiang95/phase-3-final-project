#!/usr/bin/env python3

from models import Expense
from helpers import print_main_menu, option_1

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
        menu_option = input("Select option: ")
        if menu_option.isdigit() and menu_option > '0' and menu_option < '8':
            if menu_option == '1':
                option_1(session, Expense)
            elif menu_option == '2':
                pass
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
            print(f'{menu_option} is an invalid input. Please enter a valid menu option.')
    
    session.commit()
    
    # rent_category = session.query(Category).filter_by(name='Fun').first()
    # expense = Expense(title='utilities', amount=200, category=rent_category)
    # session.add(expense)
    session.close()

    # import ipdb; ipdb.set_trace()