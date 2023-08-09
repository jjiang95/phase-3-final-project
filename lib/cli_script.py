#!/usr/bin/env python3
from models import Main

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('sqlite:///lib/database.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    print("Welcome to my CLI.")

    delete = session.query(Main).all()

    for row in delete:
        session.delete(row)
    session.commit()
    session.close()

    # import ipdb; ipdb.set_trace()