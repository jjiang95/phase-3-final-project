
# 💴 Expense Tracker 💴

Welcome to my final project of phase 3 at Flatiron, a Python-based CLI application for tracking personal expenses. Add, edit, delete, filter, export to .csv, or custom-aggregate expense entries stored in an SQL database.

## Installation

Requires `Python 3.8`. Fork this repository into your local files. `cd` into the repo and run `pipenv install`. Then, `pipenv shell` followed by `cd lib` and `./cli_script.py`. If you like, run `./seed.py` beforehand to seed the database with some generic entries. Navigate the app with arrow keys and 'enter'.

## Modules

### cli_script.py

The entry point of the app, and the file that is run directly in the terminal. Contains title display and main menu. Uses the [`simple-term-menu`](https://github.com/IngoMeyer441/simple-term-menu#create-a-menu-with-the-default-style) and [`prettycli`](https://github.com/noyoshi/prettycli) packages.

### helpers.py

`retrieve_all()` - Queries database for all data rows, sorted by date

`export_menu()` - Displays option to export filtered list/custom-selected list to .csv file, calls export() method if accepted

`export()` - Writes passed-in list of data objects to .csv file in ../exports folder of project directory

`filter_menu()` - Displays options to sort by month or category, returns either `str` or `int` selection

`filter()` - Handles filter functionality (by month or category) using returned value from `filter_menu()`

`valid_date()` - Returns True or False depending on whether passed-in number string can be converted to a `datetime` object

`validate_input()` - Checks that date and amount inputs are valid, returns list of input values

`view_all()` - Displays dynamically-generated menu for each existing entry in database; selecting any entry will lead to submenu that provides options to delete, edit, or return to main menu

`add()` - Takes in validated user input and creates + persists new expense entry in database

`edit()` - Edits any existing entry in database after it is selected from 'view all' menu

`delete()` - Deletes entry from database after it is selected from 'view all' menu

`custom_select()` - Displays multi-select menu of all existing expenses and performs custom aggregation + export option

### models.py

`class Expense(Base)` - SQLAlchemy model for primary data table; id, title, amount, date, and category id columns

`class Category(Base)` - Contains four discreet categories of expenses: Fun, Bills, Food, Misc.; linked to Expense table via foreign key in category id column of Expense

### seed.py

Run this file via `./seed.py` while in `lib` to reset database and populate with generic entries.

## Contribution

No contributions desired.

## License

[MIT](https://choosealicense.com/licenses/mit/)