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
    options = ["View all", "Add", "Filter", "Aggregate", "Exit"]
    main_menu = TerminalMenu(options, title="MAIN MENU", menu_highlight_style=("bg_black", "fg_cyan"), menu_cursor_style=("fg_blue",))
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
    # import ipdb; ipdb.set_trace()