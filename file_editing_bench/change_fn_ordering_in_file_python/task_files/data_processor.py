def process_data(data):
    """Main function to process data through multiple steps."""
    validated_data = validate_input(data)
    transformed_data = transform_data(validated_data)
    return save_results(transformed_data)

def cleanup_temp_files():
    """Utility function to clean up temporary files."""
    import os
    for file in os.listdir('/tmp'):
        if file.startswith('data_proc_'):
            os.remove(os.path.join('/tmp', file))

def save_results(processed_data):
    """Save the processed results to storage."""
    with open('output.json', 'w') as f:
        json.dump(processed_data, f)
    cleanup_temp_files()
    return True

def transform_data(data):
    """Transform the data according to business rules."""
    return {
        'processed_at': datetime.now().isoformat(),
        'values': [x * 2 for x in data['values']],
        'metadata': enrich_metadata(data['metadata'])
    }

def validate_input(data):
    """Validate the input data structure."""
    if not isinstance(data, dict):
        raise ValueError("Data must be a dictionary")
    if 'values' not in data or 'metadata' not in data:
        raise ValueError("Data must contain 'values' and 'metadata' keys")
    return data

def enrich_metadata(metadata):
    """Add additional information to metadata."""
    metadata['enriched_at'] = datetime.now().isoformat()
    metadata['version'] = '2.0'
    return metadata