class DataProcessor:
    def __init__(self, data_source):
        """Initialize the DataProcessor with a data source."""
        self.data_source = data_source
        self.processed_data = None
        self._load_cache()

    def get_raw_data(self):
        """Retrieve the raw data from the source."""
        with open(self.data_source, 'r') as f:
            return f.readlines()

    def process_data(self):
        """Process the raw data into a structured format."""
        raw_data = self.get_raw_data()
        self.processed_data = {
            str(i): float(line.strip())
            for i, line in enumerate(raw_data)
            if line.strip()
        }
        return self.processed_data

    def transform_data(self):
        """Transform the processed data using complex calculations."""
        if not self.processed_data:
            raise ValueError("No data has been processed yet!")
        
        transformed = {}
        for key, value in self.processed_data.items():
            transformed[key] = value * 2.5 + 100
        return transformed

    def save_results(self, transformed_data):
        """Save the transformed data to the output file."""
        with open(f"{self.data_source}_output.txt", 'w') as f:
            for key, value in transformed_data.items():
                f.write(f"{key}: {value}\n")

    def clear_cache(self):
        """Clear the internal cache."""
        self._cache = None
        try:
            import os
            os.remove(self.data_source + '.cache')
        except FileNotFoundError:
            pass

    def _validate_data_source(self):
        """Internal method to validate the data source format."""
        if not self.data_source.endswith('.txt'):
            raise ValueError("Data source must be a .txt file")

    def _load_cache(self):
        """Internal method to load cache from data source."""
        try:
            with open(self.data_source + '.cache', 'r') as f:
                self._cache = f.read()
        except FileNotFoundError:
            self._cache = None