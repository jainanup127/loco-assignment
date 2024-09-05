# loco-assignment

This is a Python project that manages transactions. It uses the Flask framework and SQLAlchemy for database operations.
Also leverage pydantic for data validation.

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
4. activate the virtual environment: `source venv/bin/activate`
4. Install the required packages: `pip install -r requirements.txt`
5. Run the application: `python app.py`

## Features

- Add a new transaction - O(1)
- Get a transaction by its ID - O(1)
- Get transactions by their type -O(1)
- Get the sum of a transaction and its child transactions - worst case O(n)

## UI Endpoints
Start from the root URL: `http://127.0.0.1:5000` then you can navigate to the following endpoints:
- \add
- \sum
- \type

## Running Tests

This project uses `unittest`, which is built-in to Python, to run tests. 

To run the tests, navigate to the project's root directory and run the following command:

```bash
python -m unittest
