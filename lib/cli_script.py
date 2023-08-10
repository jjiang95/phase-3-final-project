#!/usr/bin/env python3

from models import Expense, Category

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('sqlite:///database.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    print('''Expense Tracker''')

    expense = Expense()
    # category = Category(name='Misc.')
    # session.add(category)
    session.commit()
    session.close()

    # import ipdb; ipdb.set_trace()