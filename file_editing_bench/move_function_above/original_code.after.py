import logging
from typing import List, Optional

logger = logging.getLogger(__name__)


def helper_function(items: List[str]) -> List[str]:
    """Helper function that processes a list of strings."""
    return [item.strip().lower() for item in items if item]


class DataProcessor:
    def __init__(self, name: str):
        self.name = name
        self.processed_count = 0

    def process_data(self, data: List[str]) -> List[str]:
        """Main processing function that handles data transformation."""
        cleaned_data = helper_function(data)
        self.processed_count += len(cleaned_data)
        return cleaned_data

    def get_stats(self) -> dict:
        """Returns processing statistics."""
        return {"processor_name": self.name, "items_processed": self.processed_count}

    def validate_input(self, data: Optional[List[str]]) -> bool:
        """Validates the input data before processing."""
        if data is None:
            return False
        return all(isinstance(item, str) for item in data)

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
