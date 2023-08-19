#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Expense
from datetime import datetime

if __name__ == '__main__':
    engine = create_engine('sqlite:///database.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(Expense).delete()

    expenses = [
        Expense(title="Groceries",amount=125,category_id=3,date=datetime.strptime("070123", "%m%d%y")),
        Expense(title="Clothes",amount=134,category_id=4,date=datetime.strptime("070423", "%m%d%y")),
        Expense(title="Dinner",amount=174,category_id=3,date=datetime.strptime("071623", "%m%d%y")),
        Expense(title="Bowling",amount=46,category_id=1,date=datetime.strptime("072223", "%m%d%y")),
        Expense(title="Oil change",amount=66,category_id=4,date=datetime.strptime("081523", "%m%d%y")),
        Expense(title="Rent",amount=1500,category_id=2,date=datetime.strptime("090223", "%m%d%y")),
        Expense(title="Utilities",amount=130,category_id=2,date=datetime.strptime("091023", "%m%d%y")),
        Expense(title="Utilities",amount=114,category_id=2,date=datetime.strptime("082023", "%m%d%y")),
        Expense(title="Movies",amount=23,category_id=1,date=datetime.strptime("080623", "%m%d%y")),
        Expense(title="Clothes",amount=66,category_id=4,date=datetime.strptime("091423", "%m%d%y")),
        Expense(title="Lunch",amount=78,category_id=3,date=datetime.strptime("090623", "%m%d%y")),
        Expense(title="Rent",amount=1500,category_id=2,date=datetime.strptime("080223", "%m%d%y")),
        Expense(title="Rent",amount=1500,category_id=2,date=datetime.strptime("070223", "%m%d%y")),
        Expense(title="Utilities",amount=143,category_id=2,date=datetime.strptime("071023", "%m%d%y")),
    ]

    for expense in expenses:
        session.add(expense)

    session.commit()
    session.close()