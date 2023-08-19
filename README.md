
# 💴 Expense Tracker 💴

Welcome to my final project of phase 3 at Flatiron, a Python-based CLI application for tracking personal expenses. Add, edit, delete, filter, export to .csv, or custom-aggregate expense entries stored in an SQL database.

## Installation

Requires `Python 3.8`. Fork this repository into your local files. `cd` into the repo and run `pipenv install`. Then, `pipenv shell` followed by `cd lib` and `./cli_script.py`. If you like, run `./seed.py` beforehand to seed the database with some generic entries.

## Modules

### cli_script.py

The entry point of the app, and the file that is run directly in the terminal. Contains title display and main menu. Uses the [`simple-term-menu`](https://github.com/IngoMeyer441/simple-term-menu#create-a-menu-with-the-default-style) and [`prettycli`](https://github.com/noyoshi/prettycli) packages.

### helpers.py

Where the functionality of the app resides.

`retrieve_all()` - Queries database for all data rows, sorted by date

`export_menu()` - Displays option to export filtered list/custom-selected list to .csv file, calls export() method if accepted

`export()` - Writes passed-in list of data objects to .csv file in ../exports folder of project directory

`filter_menu()` - Displays options to sort by month or category, returns either `str` or `int` selection

`filter()` - Handles filter functionality using returned value from `filter_menu()`

`valid_date()` - Returns True or False depending on whether passed-in number string can be converted to a `datetime` object

`validate_input()` - Checks that date and amount inputs are valid, returns list of input values

### models.py

## Contribution

No contributions desired.

## License

[MIT](https://choosealicense.com/licenses/mit/)