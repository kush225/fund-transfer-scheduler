# Fund Transfer Scheduler

This Python script optimizes fund transfers between a parent company and its subsidiary companies based on daily bank limits and invoice amounts. It provides a schedule for transferring funds to ensure timely payments while utilizing the available daily limits efficiently.

## Requirements

- Python 3.x
- [Poetry](https://python-poetry.org/)

## Installation

1. Clone the repository:

    ```
    git clone https://github.com/kush225/fund-transfer-scheduler.git
    ```

2. Navigate to the project directory:

    ```bash
    cd fund-transfer-scheduler
    ```

3. Install dependencies using Poetry:

    ```bash
    poetry install
    ```

## Usage

1. Prepare input data in `config.py` file:
    - Define bank limits data as a dictionary with weekday, weekend, and instant wiring weekday limits for each bank.
    - Define invoices data as a dictionary with company names and corresponding invoice amounts.
    - Specify the start date for fund transfers.

2. run the `main.py`:

    ```bash
    poetry run python main.py
    ```

3. Access the transfer schedule and bank transfer schedule DataFrames for further analysis or processing.

## Test Cases

The `test_data` in `test_data.py` file contains test cases to ensure the correctness of the fund transfer algorithm. Each test case includes bank limits data, invoices data, start date, and expected transfer schedule data.

1. To run the test cases, execute the test script using 

    ```bash
    poetry run python test.py 
    ```

