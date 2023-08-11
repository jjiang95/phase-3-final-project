from sqlalchemy import (Column, String, Integer, ForeignKey, DateTime)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer(), primary_key=True)
    title = Column(String())
    amount = Column(Integer())
    date = Column(DateTime)
    category_id = Column(Integer(), ForeignKey('categories.id'))

    category = relationship('Category', back_populates='expenses')
    
    def format_date(self):
        return self.date.strftime("%m/%y")

    def __repr__(self):
        return f'Title: {self.title} | Amount: {self.amount} | Category: {self.category.name} | Date: {self.format_date()}'

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer(), primary_key=True)
    name = Column(String(), unique=True, nullable=False)

    expenses = relationship(Expense, back_populates='category')