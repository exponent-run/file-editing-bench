# Function Ordering Task

Reorder the methods in the `DataProcessor` class to follow a logical sequence. The methods should be ordered as follows:

1. `__init__` should be the first method (as per Python conventions)
2. Main public interface methods should come next, ordered by importance:
   - `process_batch` (main processing method)
   - `get_stats` (public status method)
   - `cleanup_temp_files` (public utility method)
3. Private implementation methods should come last, in the order they are used in the processing flow:
   - `validate_data` (first step in processing)
   - `transform_data` (second step in processing)
   - `save_results` (final step in processing)

Do not modify any of the method implementations - only change their order within the class.