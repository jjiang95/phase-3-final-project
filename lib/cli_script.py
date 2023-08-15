#!/usr/bin/env python3

from models import Expense
from helpers import view_all, add, filter

from simple_term_menu import TerminalMenu
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def main():
    print("\n" * 30)
    print('''
$$$$$$$$\                                                                   $$$$$$$$\                           $$\                           
$$  _____|                                                                  \__$$  __|                          $$ |                          
$$ |      $$\   $$\  $$$$$$\   $$$$$$\  $$$$$$$\   $$$$$$$\  $$$$$$\           $$ | $$$$$$\  $$$$$$\   $$$$$$$\ $$ |  $$\  $$$$$$\   $$$$$$\  
$$$$$\    \$$\ $$  |$$  __$$\ $$  __$$\ $$  __$$\ $$  _____|$$  __$$\          $$ |$$  __$$\ \____$$\ $$  _____|$$ | $$  |$$  __$$\ $$  __$$\ 
$$  __|    \$$$$  / $$ /  $$ |$$$$$$$$ |$$ |  $$ |\$$$$$$\  $$$$$$$$ |         $$ |$$ |  \__|$$$$$$$ |$$ /      $$$$$$  / $$$$$$$$ |$$ |  \__|
$$ |       $$  $$<  $$ |  $$ |$$   ____|$$ |  $$ | \____$$\ $$   ____|         $$ |$$ |     $$  __$$ |$$ |      $$  _$$<  $$   ____|$$ |      
$$$$$$$$\ $$  /\$$\ $$$$$$$  |\$$$$$$$\ $$ |  $$ |$$$$$$$  |\$$$$$$$\          $$ |$$ |     \$$$$$$$ |\$$$$$$$\ $$ | \$$\ \$$$$$$$\ $$ |      
\________|\__/  \__|$$  ____/  \_______|\__|  \__|\_______/  \_______|         \__|\__|      \_______| \_______|\__|  \__| \_______|\__|      
                    $$ |                                                                                                                      
                    $$ |                                                                                                                      
                    \__|                                                                                                                      
    ''')
    main_menu_options = ["View all", "Add", "Filter", "Aggregate", "Exit"]
    main_menu = TerminalMenu(main_menu_options, title="MAIN MENU", menu_highlight_style=("bg_black", "fg_cyan", "bold"), menu_cursor_style=("fg_blue",))
    while True:
        print()
        main_menu_index = main_menu.show()
        if main_menu_options[main_menu_index] == "View all":
            view_all(session, Expense)
        elif main_menu_options[main_menu_index] == "Add":
            add(session, Expense)
        elif main_menu_options[main_menu_index] == "Filter":
            filter(session, Expense)
        elif main_menu_options[main_menu_index] == "Aggregate":
            pass
        elif main_menu_options[main_menu_index] == "Exit":
            print('EXITING...')
            break   

if __name__ == '__main__':
    engine = create_engine('sqlite:///database.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    main()
    # import ipdb; ipdb.set_trace()