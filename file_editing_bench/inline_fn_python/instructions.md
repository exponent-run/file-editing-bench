# Inline Function Task

## Task Description
In the file `customer_processor.py`, inline the helper function `calculate_discount_multiplier` directly into the `process_customer_purchase` function where it is called. After inlining, delete the original helper function.

## Requirements
1. Move all the logic from `calculate_discount_multiplier` into `process_customer_purchase` where the `multiplier = calculate_discount_multiplier(...)` line is
2. Preserve all comments from the helper function
3. Delete the original `calculate_discount_multiplier` function completely
4. Maintain the exact same functionality and calculations
5. Keep the same variable names from the helper function

The final code should produce identical results for all inputs, just with the helper function's logic moved inline to where it was called.