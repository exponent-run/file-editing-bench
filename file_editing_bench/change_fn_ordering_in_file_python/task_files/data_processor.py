def transform_data(data):
    """Transform the processed data into the final format."""
    transformed = {k: v * 2 for k, v in data.items()}
    return transformed

def load_data(filepath):
    """Load data from a file."""
    with open(filepath, 'r') as f:
        data = {}
        for line in f:
            key, value = line.strip().split(',')
            data[key] = float(value)
    return data

def save_results(filepath, results):
    """Save the final results to a file."""
    with open(filepath, 'w') as f:
        for key, value in results.items():
            f.write(f"{key},{value}\n")

def validate_data(data):
    """Validate the loaded data."""
    if not isinstance(data, dict):
        raise ValueError("Data must be a dictionary")
    for key, value in data.items():
        if not isinstance(value, (int, float)):
            raise ValueError(f"Value for key {key} must be numeric")
    return data

def process_data(data):
    """Process the validated data."""
    processed = {}
    for key, value in data.items():
        if value < 0:
            processed[key] = abs(value)
        else:
            processed[key] = value
    return processed