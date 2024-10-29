# Function Reordering Task

Reorder the functions in `data_processor.py` to follow a logical flow and improve code readability. The functions should be ordered as follows:

1. Input validation functions should come first (`validate_input`)
2. Helper/utility functions should come next (`enrich_metadata`)
3. Core processing functions should follow (`transform_data`)
4. Output/storage related functions next (`save_results`, `cleanup_temp_files`)
5. Main orchestrator function should be last (`process_data`)

The content of each function should remain exactly the same - only their order in the file should change.

This ordering follows the principle of having lower-level utilities first, followed by higher-level functions that use them, with the main entry point at the end.