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
            expected_company_transfer_data = data['expected_company_transfer_data']
            expected_bank_transfer_data = data['expected_bank_transfer_data']
            start_date = datetime.strptime(data['start_date'], '%Y-%m-%d')

            # Convert input data to DataFrames
            bank_limits = pd.DataFrame(bank_limits_data)
            bank_limits.fillna(0, inplace=True)
            invoices = pd.DataFrame(invoices_data)

            # Call the function to transfer funds
            bank_log_schedule, company_log_schedule = transfer_funds(start_date, invoices, bank_limits )

            bank_log_schedule.fillna(0, inplace=True)
            company_log_schedule.fillna(0, inplace=True) 
            
            index_labels = {start_date + timedelta(days=x): x for x in range(6)}

            # Create the DataFrame with expected transfer schedule data and indexed by dates
            expected_company_log_df = pd.DataFrame(data=expected_company_transfer_data, index=index_labels, dtype=float)
            expected_bank_log_df = pd.DataFrame(data=expected_bank_transfer_data, index=index_labels, dtype=float)

            # Compare actual results with expected results
            assert company_log_schedule.equals(expected_company_log_df)  
            assert bank_log_schedule.equals(expected_bank_log_df) 
            assert invoices['Amount'].sum() == 0 


if __name__=='__main__':
	unittest.main()
