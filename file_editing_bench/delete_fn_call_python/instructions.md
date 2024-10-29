# Delete Validation Function

In the file `data_processor.py`, there is a helper method `_validate_data_format` that performs validation checks on incoming data. Your task is to:

1. Remove the entire `_validate_data_format` helper method
2. Remove the validation check in the `process_metrics_batch` method (specifically, remove the if statement that uses this validation function)

The code should process all data items in the batch without any validation checks.