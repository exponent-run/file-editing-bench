import pandas as pd
from typing import List, Dict
import numpy as np
from datetime import datetime

def process_sales_data(data: pd.DataFrame) -> pd.DataFrame:
    """Process raw sales data into aggregated format"""
    return data.groupby('product_id').agg({
        'quantity': 'sum',
        'price': 'mean'
    }).reset_index()

def calculate_revenue_impact(sales: pd.DataFrame, 
                           costs: pd.DataFrame) -> Dict[str, float]:
    """Calculate revenue impact by product category"""
    merged = sales.merge(costs, on='product_id', how='left')
    merged['profit'] = (merged['price'] - merged['cost']) * merged['quantity']
    return merged.groupby('category')['profit'].sum().to_dict()

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

def main():
    # Example usage
    sales_data = pd.DataFrame({
        'product_id': [1, 2, 1, 3],
        'quantity': [5, 3, 2, 1],
        'price': [10.0, 15.0, 10.0, 25.0],
        'date': ['2023-01-01', '2023-01-02', '2023-01-01', '2023-01-03']
    })
    
    processed = process_sales_data(sales_data)
    dates = sales_data['date'].tolist()
    valid = validate_transaction_dates(dates)
    print(f"Processed data shape: {processed.shape}")
    print(f"Valid dates: {valid}")

if __name__ == "__main__":
    main()