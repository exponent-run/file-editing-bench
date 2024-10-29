# Rename Variables Across Functions

In the file `token_processor.ex`, there is a variable named `tkn` that is used across multiple functions. This abbreviated name is not descriptive enough and should be renamed to `token` across all functions to improve code readability.

The variable appears in the following functions:
- As a parameter in `process_token/1`
- As a parameter in `decode_token/1`
- As a parameter in `validate_token/1`
- As a parameter in `enrich_token_data/1`
- In various function bodies where the parameter is used

Rename all occurrences of `tkn` to `token` while maintaining the exact same functionality. Make sure to update all instances consistently.