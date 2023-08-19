
# 💴 Expense Tracker 💴

Welcome to my final project of phase 3 at Flatiron! This is a Python-based CLI application for tracking personal expenses. Add, edit, delete, filter, export, or custom-aggregate expense entries stored in an SQL database.

## Installation

Requires `Python 3.8`. Fork this repository into your local files. `cd` into the repo and run `pipenv install`. Then, `pipenv shell` followed by `cd lib` and `./cli_script.py`. If you like, run `./seed.py` beforehand to seed the database with some generic entries.

## Modules

### cli_script.py

The entry point of the app, and the file that is run directly in the terminal. Contains title display and main menu. Uses the [`simple-term-menu`](https://github.com/IngoMeyer441/simple-term-menu#create-a-menu-with-the-default-style) and [`prettycli`](https://github.com/noyoshi/prettycli) packages.

### helpers.py

Where the functionality of the app resides. 

### models.py

## Contribution

No contributions desired.

## License

[MIT](https://choosealicense.com/licenses/mit/)