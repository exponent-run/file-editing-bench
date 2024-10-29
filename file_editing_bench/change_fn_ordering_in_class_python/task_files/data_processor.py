class DataProcessor:
    def process_batch(self, data_batch):
        """Process a batch of data records."""
        validated_data = self.validate_data(data_batch)
        transformed = self.transform_data(validated_data)
        return self.save_results(transformed)

    def cleanup_temp_files(self):
        """Remove any temporary files created during processing."""
        import os
        for file in os.listdir(self.temp_dir):
            if file.endswith('.tmp'):
                os.remove(os.path.join(self.temp_dir, file))

    def __init__(self, temp_dir="/tmp"):
        """Initialize the data processor."""
        self.temp_dir = temp_dir
        self.processed_count = 0

    def save_results(self, processed_data):
        """Save the processed results to storage."""
        self.processed_count += len(processed_data)
        return [item.get('id') for item in processed_data]

    def transform_data(self, data):
        """Transform the validated data into the required format."""
        return [
            {
                'id': item['id'],
                'value': item['raw_value'] * 2,
                'timestamp': item['timestamp'].isoformat()
            }
            for item in data
        ]

    def get_stats(self):
        """Return processing statistics."""
        return {
            'processed_count': self.processed_count,
            'temp_dir': self.temp_dir
        }

    def validate_data(self, data):
        """Validate the input data format."""
        valid_records = []
        for record in data:
            if all(k in record for k in ['id', 'raw_value', 'timestamp']):
                valid_records.append(record)
        return valid_records