import json
from datetime import datetime
from typing import Dict, List, Optional
from urllib.parse import urlparse
import requests
from pathlib import Path

def load_config(config_path: str) -> Dict:
    """Load configuration from a JSON file."""
    with open(config_path) as f:
        return json.load(f)

def parse_url_components(url: str) -> Dict[str, str]:
    """Extract components from a URL."""
    parsed = urlparse(url)
    return {
        "scheme": parsed.scheme,
        "netloc": parsed.netloc,
        "path": parsed.path,
        "params": parsed.params,
        "query": parsed.query,
        "fragment": parsed.fragment
    }

def fetch_remote_data(endpoint: str) -> Optional[Dict]:
    """Fetch data from a remote endpoint using requests."""
    try:
        response = requests.get(endpoint, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException:
        return None

def format_timestamp(timestamp: float) -> str:
    """Convert a Unix timestamp to ISO format."""
    return datetime.fromtimestamp(timestamp).isoformat()

def process_log_files(log_dir: str) -> List[Dict]:
    """Process all log files in a directory."""
    results = []
    for log_file in Path(log_dir).glob("*.log"):
        with open(log_file) as f:
            results.extend(json.loads(line) for line in f)
    return results