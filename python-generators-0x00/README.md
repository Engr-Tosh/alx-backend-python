# Python Generators — ALX Backend Project

This directory contains scripts and utilities related to Python generators, used to interact with MySQL databases in a memory-efficient manner.

## Tasks

* **Database Setup & Seeding**: Scripts to create a MySQL database, create tables, and insert seed data from CSV.
* **Streaming Generator**: Uses a generator to yield rows from the `user_data` table one at a time using `yield`.

## Highlights

* Secure database credentials via `.env` and `python-dotenv`
* MySQL connector with proper error handling and cursor management
* Generator-based iteration for scalable row streaming

More tasks will be added and the README refined as progress continues.

---

> Make sure to activate your virtual environment and install dependencies manually for now using:
> `pip install mysql-connector-python python-dotenv`
> A `requirements.txt` file will be added later.

