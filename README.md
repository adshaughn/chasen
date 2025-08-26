# chasen

## Chasen is a Python-based application designed for tea drinkers.

## Key Features

### Brewing guide

The brewing guide is the user-guided tea assistant. It will ask questions to guide the user as they brew. It will also
update the two underlying tables, the Log and the Stock.

### Journal/log

The core functionality of Chasen is as a tea log.

There are two tables in Chasen:

1) a running journal of teas, so the user can record details about each tea session. This table includes:

- Date and time (datetime)
- Name of tea (string)
- Type of tea (string)
- Source / vendor of tea (string)
- Quantity used (int)
- Tasting notes (string)

2) a stocklist of teas, so the user can keep track of which teas they have in their collection, and how much they still
   have on-hand. This table includes:

- Name (string)
- Type (string)
- Subtype (string)
- Source (string)
- Quantity on hand (int)
- Recommended water (int)
- Recommended amount (int)
- Recommended steeping temperature (int)
- Recommended steeping time (int)

The user inputs string data through a guided flow which is added as an entry into the log table.

### Recommendation engine

As a stretch goal, Chasen will include a recommendation engine. The user will be able to ask Chasen to x. Based on this
user information, the app will be able to perform analyses on tasting notes from previous sessions to come up with a
suggestion.

This may eventually include data from other sources like steepster.com, so the app can recommend teas even if the user
has never tried them. ("Would you like to have something familiar or something new?")

## Tech Stack

Python 3.11

## Packages

### Runtime
- tabulate==0.9.0

### Development
- pytest==8.2.2
- black==24.4.2
- isort==5.13.2
- flake8==7.0.0

### Planned (future features)
- pandas==2.2.2
- python-dateutil==2.9.0
- pydantic==2.6.4
- rich==13.7.1
- APScheduler==3.10.4
- simpleaudio==1.0.4

## Installation Instructions and User Guide

uv pip install -e .

## Structure

chasen/
├── chasen/                  # Main source code
│   ├── init.py
│   ├── chasen_app.py        # Entry point for the application
│   ├── inventory.py         # Tea inventory management (SQLite + tabulate)
│   ├── journal.py           # Tea journal logging (WIP)
│   ├── timer.py             # Tea brewing timer (WIP)

├── data/
│   └── chasen.db            # SQLite database file
│
├── tests/                   # Unit tests (pytest) (mirrors code structure)
│   ├── init.py
│   ├── test_inventory.py
│   └── test_journal.py
│
├── main.py                  # CLI launcher for Chasen
├── pyproject.toml           # Project dependencies & config (uv/black/pytest)
├── README.md                # Project documentation
└── .gitignore               # Git ignore rules

## Development Roadmap

Initial development will be focused on the logging features.

Currently working on implementing the stock table with associated tests.

## Licenses

## Acknowledgements
