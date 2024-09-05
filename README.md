# loco-assignment

This is a Python project that manages transactions. It uses the Flask framework and SQLAlchemy for database operations.

## Project Structure

- `transaction/` - This directory contains the main transaction management logic.
  - `models/` - Contains the `Transaction` model.
  - `repositories/` - Contains the `TransactionRepository` which handles database operations.
  - `services/` - Contains the `TransactionService` which contains business logic.
  - `adaptors/` - Contains the `TransactionAdaptor` which is used for converting entities to DTOs.

## Setup

1. Clone the repository: `git clone`
2. Navigate to the project's root directory: `cd loco-assignment`
3. Create a virtual environment: `python -m venv venv`
4. Install the required packages: `pip install -r requirements.txt`
5. Run the application: `python app.py`

## Features

- Add a new transaction
- Get a transaction by its ID
- Get transactions by their type
- Get the sum of a transaction and its child transactions

## Running Tests

This project uses `unittest`, which is built-in to Python, to run tests. 

To run the tests, navigate to the project's root directory and run the following command:

```bash
python -m unittest
