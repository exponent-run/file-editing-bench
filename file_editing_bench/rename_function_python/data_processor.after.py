import json
from typing import Dict, List, Any
from datetime import datetime

def process_and_standardize_records(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Process a list of data records by:
    1. Removing any empty records
    2. Adding a timestamp field
    3. Converting all string values to uppercase
    """
    processed = []
    for record in data:
        if record:  # Skip empty records
            # Add timestamp
            record['processed_at'] = datetime.now().isoformat()
            
            # Convert string values to uppercase
            processed_record = {}
            for key, value in record.items():
                if isinstance(value, str):
                    processed_record[key] = value.upper()
                else:
                    processed_record[key] = value
            
            processed.append(processed_record)
    
    return processed

def load_json_file(filepath: str) -> Dict[str, Any]:
    """Load and parse a JSON file."""
    with open(filepath, 'r') as f:
        return json.load(f)

def save_json_file(data: Dict[str, Any], filepath: str) -> None:
    """Save data to a JSON file."""
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)