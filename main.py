from datetime import datetime, timedelta, date
import pandas as pd
from typing import Dict, List
from config import start_date,  bank_limits_data, invoices_data

bank_limits = pd.DataFrame(bank_limits_data)
bank_limits.fillna(0, inplace=True)
invoices = pd.DataFrame(invoices_data)

# Initialize company transfer log and bank transfer log
company_transfer_log = pd.DataFrame(columns=invoices_data['Company'])
bank_transfer_log = pd.DataFrame(columns=["Bank 1", "Bank 2", "Bank 3", "Bank 4"]) 
save_transactions = True

def transfer(invoices: pd.DataFrame,
             data: Dict[str, int], 
             limit: int, 
             bank_transfered: List[int], 
             total_transferred: int = 0) -> int:
    """
    Perform fund transfer for invoices based on the available bank limit.
    
    Args:
        invoices (pd.DataFrame): Dataframe object representing the invoices data
        data (Dict[str, int]): Dictionary containing company names and their transferred amounts.
        limit (int): Available transfer limit for the bank.
        bank_transfered (List[int]): List to store transfer amounts for the current bank.
        total_transferred (int): Total amount transferred across all banks.
        
    Returns:
        total_transferred (int): Total amount transferred across all banks.
    """
    for idx, row in invoices.iterrows():
        company, amount = row['Company'], row['Amount']
        
        # Transfer amount limited by the available bank limit
        transfer_amount = min(amount, limit)
        data[company] = data.get(company, 0) + transfer_amount
        bank_transfered.append(transfer_amount)
        invoices.loc[idx, 'Amount'] -= transfer_amount
        total_transferred += transfer_amount
        limit -= transfer_amount
        
        if limit <= 0:
            break

    return total_transferred 

def transfer_funds(start_date: datetime, invoices: pd.DataFrame, bank_limits: pd.DataFrame) -> date:
    """
    Perform fund transfers for invoices across multiple banks until all invoices are paid.
    
    Args:
        start_date (datetime): The start date for fund transfers.
        invoices (pd.DataFrame): Dataframe object representing the invoices data.
        bank_limits (pd.DataFrame): Dataframe object representing the bank limits data.
        
    Returns:
        completion_date (date): The completion date when all invoices are paid.
    """
    total_transferred: int = 0

    # Loop until all invoices are paid
    while invoices['Amount'].sum() > 0:
        # Determine the column to use for bank limits based on the current date
        weekday_type: str = 'weekday' if start_date.weekday() < 5 else 'weekend'
        # Sort banks by the available limit in descending order
        bank_limits.sort_values(by=weekday_type, ascending=False, inplace=True)
        data: Dict[str, int] = {}
        bank_data: Dict[str, int] = {}
        
        # Iterate over banks to transfer funds
        for bank_name, limit in bank_limits.iterrows():
            bank_transfered: List[int] = []
            limit: int = limit[weekday_type]
            
            # Perform fund transfer
            total_transferred += transfer(invoices, data, limit, bank_transfered)
            bank_data[bank_name] = bank_data.get(bank_name, 0 ) + sum(bank_transfered)

        # use instant_wiring_weekday if bank limit is reached and amount to transfer is remaining
        for bank_name, limit in bank_limits.iterrows():
            bank_transfered: List[int] = []
            limit: int = limit["instant_wiring_weekday"]

            if not limit:
                continue
            
            # Perform fund transfer
            total_transferred += transfer(invoices, data, limit, bank_transfered)
            bank_data[bank_name] = bank_data.get(bank_name, 0 ) + sum(bank_transfered)

            
        # Update transfer and bank transfer schedule
        company_transfer_log.loc[start_date.date()] = data
        bank_transfer_log.loc[start_date.date()] = bank_data
        start_date += timedelta(days=1)

    completion_date = company_transfer_log.index[-1]
    
    return completion_date


def main():
    completion_date = transfer_funds(start_date, invoices, bank_limits)

    # saving transaction logs
    if save_transactions:
        company_transfer_log.reset_index(inplace=True)
        company_transfer_log.rename(columns={'index': 'completion_date'},inplace=True)
        company_transfer_log.to_csv('company_transfer.csv', index=False)

        bank_transfer_log.reset_index(inplace=True)
        bank_transfer_log.rename(columns={'index': 'completion_date'},inplace=True)
        bank_transfer_log.to_csv('bank_transfer.csv', index=False)

    # Print the final results
    # print("Invoice Job Startdate:", start_date.date() )
    # print("\n")
    # print("###Bank Transfer details")
    # print(bank_transfer_log)
    # print("\n")
    # print("###Company Transfer details\n")
    # print(company_transfer_log)
    # print("\n")

    print("Invoice Job Completion date:", completion_date ) 


if __name__ == "__main__":
    main()