from sqlalchemy import (Column, String, Integer)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Main(Base):
    __tablename__ = "main"

    id = Column(Integer(), primary_key=True)
    title = Column(String())
    amount = Column(Integer())