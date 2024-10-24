import logging
from typing import List, Optional

logger = logging.getLogger(__name__)

class DataProcessor:
    def __init__(self, name: str):
        self.name = name
        self.processed_count = 0
    
    def process_data(self, data: List[str]) -> List[str]:
        """Main processing function that handles data transformation."""
        if not self.validate_input(data):
            raise ValueError("Invalid input data")
        cleaned_data = [item.strip().lower() for item in data if item]
        self.processed_count += len(cleaned_data)
        return cleaned_data
    
    def get_stats(self) -> dict:
        """Returns processing statistics."""
        return {
            "processor_name": self.name,
            "items_processed": self.processed_count
        }
    
    def validate_input(self, data: Optional[List[str]]) -> bool:
        """Validates the input data before processing."""
        if data is None:
            return False
        return all(isinstance(item, str) for item in data)
    
    def deprecated_method(self) -> None:
        """This method is deprecated and should be removed."""
        logger.warning("Using deprecated method")
        self.processed_count = 0
    
    def clear_stats(self) -> None:
        """Resets the processing statistics."""
        self.processed_count = 0

def main():
    processor = DataProcessor("default")
    sample_data = ["  Hello  ", "World  ", "  Python"]
    result = processor.process_data(sample_data)
    print(f"Processed data: {result}")
    print(f"Stats: {processor.get_stats()}")

if __name__ == "__main__":
    main()