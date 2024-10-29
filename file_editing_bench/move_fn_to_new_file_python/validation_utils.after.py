from typing import List
from datetime import datetime

def validate_transaction_dates(dates: List[str]) -> List[bool]:
    """Validate a list of transaction dates"""
    valid_dates = []
    for date_str in dates:
        try:
            datetime.strptime(date_str, '%Y-%m-%d')
            valid_dates.append(True)
        except ValueError:
            valid_dates.append(False)
    return valid_dates