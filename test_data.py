data = [
    {
        'bank_limits_data': { 
            "weekday": {"Bank 1": 20000, "Bank 2": 50000, "Bank 3": 100000, "Bank 4": 100000},
            "weekend": {"Bank 1": 100000, "Bank 2": 50000, "Bank 3": 100000, "Bank 4": 50000},
            "instant_wiring_weekday": {"Bank 2": 10000}
        },
        'invoices_data': {
            'Company': ['Company 1', 'Company 2', 'Company 3', 'Company 4', 'Company 5', 'Company 6'],
            'Amount': [250000, 200000, 165000, 430000, 301000, 192000]
        },
        'start_date': '2024-01-01',
        'expected_company_transfer_data': {
            'Company 1': [250000, 0, 0, 0, 0, 0],
            'Company 2': [30000, 170000, 0, 0, 0, 0],
            'Company 3': [0, 110000, 55000, 0, 0, 0],
            'Company 4': [0, 0, 225000, 205000, 0, 0],
            'Company 5': [0, 0, 0, 75000, 226000, 0],
            'Company 6': [0, 0, 0, 0, 54000, 138000]
        },
        'expected_bank_transfer_data': {
            "Bank 1": [20000, 20000, 20000, 20000, 20000, 38000],
            "Bank 2": [60000, 60000, 60000, 60000, 60000, 0],
            "Bank 3": [100000, 100000, 100000, 100000, 100000, 100000],
            "Bank 4": [100000, 100000, 100000, 100000, 100000, 0]
        }
    },
]
