# Move Utility Functions Task

## Task Description

You have a document processing system split across two files:
- `document_processor.py`: Contains the main business logic
- `utils.py`: Contains utility functions

Your task is to move all utility functions except `generate_document_id()` from `utils.py` into `document_processor.py`. The `generate_document_id()` function should remain in `utils.py`.

## Specific Requirements

1. Move these functions from `utils.py` to `document_processor.py`:
   - `calculate_checksum()`
   - `format_timestamp()`
   - `sanitize_filename()`
   - `parse_metadata()`
   - `validate_document_type()`

2. Leave this function in `utils.py`:
   - `generate_document_id()`

3. Update all imports in both files:
   - Remove unused imports from `utils.py`
   - Add any necessary imports to `document_processor.py`
   - Update the import statement in `document_processor.py` to only import `generate_document_id`

4. Maintain the exact same functionality - only the location of the functions should change.

## Success Criteria

1. All functions except `generate_document_id()` are moved to `document_processor.py`
2. `generate_document_id()` remains in `utils.py`
3. All imports are correctly updated in both files
4. The DocumentProcessor class continues to work exactly as before
5. No changes are made to the actual implementation of any functions