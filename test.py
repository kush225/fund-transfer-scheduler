import pandas as pd
from datetime import datetime, timedelta
from main import transfer_funds
import unittest
from test_data import data as test_data

# Define test function
class TestPrime(unittest.TestCase):
    def test_transfer_funds_with_test_data(self):
        for data in test_data:
            # Extract input data
            bank_limits_data = data['bank_limits_data']
            invoices_data = data['invoices_data']
            expected_completion_date = datetime.strptime(data['completion_date'], '%Y-%m-%d')
            start_date = datetime.strptime(data['start_date'], '%Y-%m-%d')

            # Convert input data to DataFrames
            bank_limits = pd.DataFrame(bank_limits_data)
            bank_limits.fillna(0, inplace=True)
            invoices = pd.DataFrame(invoices_data)

            # Call the function to transfer funds
            actual_completion_date = transfer_funds(start_date, invoices, bank_limits )

            assert expected_completion_date.date() == actual_completion_date
            assert invoices['Amount'].sum() == 0 

if __name__=='__main__':
	unittest.main()
