from datetime import datetime 
from typing import Dict, List, Union

# Initialize start date
start_date: datetime = datetime(2024, 1, 1)

# Define the daily limits for each bank account
bank_limits_data: Dict[str, Dict[str, int]] = { 
    "weekday": {"Bank 1": 200000, "Bank 2": 50000, "Bank 3": 200000, "Bank 4": 100000},
    "weekend": {"Bank 1": 100000, "Bank 2": 50000, "Bank 3": 100000, "Bank 4": 50000},
    "instant_wiring_weekday": {"Bank 2": 50000}
}

# Define the invoices for each subsidiary company
invoices_data: Dict[str, List[Union[str, int]]] = {
    'Company': ['Company 1', 'Company 2', 'Company 3', 'Company 4', 'Company 5', 'Company 6'],
    'Amount': [214000, 372000, 112000, 72000, 198000, 97000]
}