import json
from typing import List, Dict

DEFAULT_CONFIG = {
    "batch_size": 100,
    "max_retries": 3,
    "timeout_ms": 5000,
    "data_format": "json"
}

def load_data(filepath: str) -> List[Dict]:
    with open(filepath, 'r') as f:
        data = json.load(f)
    
    if len(data) > DEFAULT_CONFIG["batch_size"]:
        print(f"Warning: Data exceeds DEFAULT_CONFIG batch size of {DEFAULT_CONFIG['batch_size']}")
    
    return data[:DEFAULT_CONFIG["batch_size"]]

def process_batch(batch: List[Dict]) -> List[Dict]:
    results = []
    retries = 0
    
    while retries < DEFAULT_CONFIG["max_retries"]:
        try:
            for item in batch:
                if DEFAULT_CONFIG["data_format"] == "json":
                    processed = {k: str(v).upper() if isinstance(v, str) else v 
                               for k, v in item.items()}
                    results.append(processed)
            break
        except Exception as e:
            retries += 1
            if retries == DEFAULT_CONFIG["max_retries"]:
                raise Exception(f"Failed after {DEFAULT_CONFIG['max_retries']} retries")
    
    return results

def main():
    data = load_data("input.json")
    processed = process_batch(data)
    print(f"Processed {len(processed)} items using {DEFAULT_CONFIG['data_format']} format")

if __name__ == "__main__":
    main()