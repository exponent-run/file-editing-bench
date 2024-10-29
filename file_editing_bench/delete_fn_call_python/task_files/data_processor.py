class DataProcessor:
    def __init__(self, config):
        self.config = config
        self.processed_count = 0
    
    def _validate_data_format(self, data):
        """Helper function to validate data format before processing"""
        if not isinstance(data, dict):
            return False
        required_fields = ['timestamp', 'metrics', 'source']
        return all(field in data for field in required_fields)
    
    def process_metrics_batch(self, batch_data):
        """Process a batch of metrics data"""
        results = []
        for data in batch_data:
            if not self._validate_data_format(data):
                continue
                
            processed = {
                'timestamp': data['timestamp'],
                'metrics': {
                    k: v * self.config.get('scaling_factor', 1.0)
                    for k, v in data['metrics'].items()
                },
                'source': data['source'],
                'processed_at': time.time()
            }
            results.append(processed)
            self.processed_count += 1
            
        return results