from sqlalchemy import (Column, String, Integer, ForeignKey)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer(), primary_key=True)
    title = Column(String())
    amount = Column(Integer())
    category_id = Column(Integer(), ForeignKey('categories.id'))

    category = relationship('Category', back_populates='expenses')

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer(), primary_key=True)
    name = Column(String(), unique=True, nullable=False)

    expenses = relationship(Expense, back_populates='category')