# Python Generators Project

This directory contains Python scripts and resources developed to practice and demonstrate the use of Python generators, database interaction, and other backend concepts.

## Current Script(s)

### `main.py`

* Establishes a connection to a MySQL server
* Creates a database (`ALX_prodev`) if it does not exist
* Creates a table `user_data` with the following fields:

  * `user_id` (Auto-increment Primary Key)
  * `name` (VARCHAR)
  * `email` (VARCHAR)
  * `age` (DECIMAL)
* Inserts sample data from a CSV file into the table
* Fetches and prints the first 5 records

### `seed.py`

* Contains reusable functions for:

  * Connecting to MySQL server
  * Creating database and tables
  * Connecting to the `ALX_prodev` database
  * Inserting data into the `user_data` table

## Directory Structure

```
python-generators-0x00/
├── main.py
├── seed.py
├── user_data.csv
└── README.md
```

## Requirements

* Python 3.10+
* `mysql-connector-python`
* MySQL server running locally

## Notes

This README will be updated and refined as more scripts and generator-based features are added to this project.
