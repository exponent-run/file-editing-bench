from typing import List, Dict
from datetime import datetime


def standardize_records(records: List[Dict]) -> List[Dict]:
    """Process and standardize records by:
    - Filtering out empty records
    - Adding timestamps
    - Converting string values to uppercase
    """
    result = []
    for record in records:
        if record and validate_record(record):
            processed = record.copy()
            processed['timestamp'] = datetime.now().isoformat()
            processed['type'] = processed['type'].upper()
            result.append(processed)
    return result


def validate_record(record: Dict) -> bool:
    """Validate that a record has all required fields"""
    return all(k in record for k in ['id', 'value', 'type'])


def sort_records(records: List[Dict], key: str = 'id') -> List[Dict]:
    """Sort records by the specified key"""
    return sorted(records, key=lambda x: x.get(key, ''))