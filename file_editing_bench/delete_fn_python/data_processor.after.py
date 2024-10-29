import json
from datetime import datetime
from typing import Dict, List, Optional
from urllib.parse import urlparse
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

def format_timestamp(dt: datetime) -> str:
    """Format a datetime object into a standardized string."""
    return dt.strftime("%Y-%m-%d %H:%M:%S UTC")

def process_log_files(log_dir: str) -> List[Dict]:
    """Process all log files in a directory."""
    results = []
    log_path = Path(log_dir)
    for file in log_path.glob("*.log"):
        with open(file) as f:
            results.extend(json.loads(line) for line in f)
    return results