import json
from datetime import datetime
from typing import Dict, List, Optional
from urllib.parse import urlparse  # This import will need to be removed
import pandas as pd

def load_json_data(filepath: str) -> Dict:
    """Load data from a JSON file."""
    with open(filepath, 'r') as f:
        return json.load(f)

def extract_domain(url: str) -> str:
    """Extract domain from URL - this function will be deleted."""
    parsed = urlparse(url)
    return parsed.netloc

def process_timestamps(data: List[Dict]) -> List[Dict]:
    """Convert timestamp strings to datetime objects."""
    for item in data:
        if 'timestamp' in item:
            item['timestamp'] = datetime.fromisoformat(item['timestamp'])
    return data

def calculate_metrics(df: pd.DataFrame) -> Dict[str, float]:
    """Calculate basic statistical metrics."""
    return {
        'mean': df['value'].mean(),
        'median': df['value'].median(),
        'std': df['value'].std()
    }

def export_results(data: Dict[str, float], output_path: Optional[str] = None) -> None:
    """Export results to JSON file."""
    output_path = output_path or 'results.json'
    with open(output_path, 'w') as f:
        json.dump(data, f, indent=2)