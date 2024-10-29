class DataProcessor:
    def __init__(self, config):
        self.config = config
        self.processed_count = 0
    
    def process_metrics_batch(self, batch_data):
        """Process a batch of metrics data"""
        results = []
        for data in batch_data:
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