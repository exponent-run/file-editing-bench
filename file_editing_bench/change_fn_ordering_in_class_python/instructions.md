# Task: Reorder Methods in DataProcessor Class

Reorder the methods in the `DataProcessor` class to follow this logical grouping and sequence:

1. First should be the constructor (`__init__`)
2. Then public interface methods in order of typical usage:
   - get_raw_data
   - process_data
   - transform_data
   - save_results
   - clear_cache
3. Finally, private helper methods (prefixed with _) at the bottom:
   - _validate_data_source
   - _load_cache

The content and implementation of each method should remain exactly the same - only their order in the file should change.

This ordering reflects a more logical organization where:
- Constructor is first
- Public methods are grouped together
- Private helper methods are grouped at the end