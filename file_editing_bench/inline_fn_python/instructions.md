# Inline Function Task

## Task Description
In the file `customer_processor.py`, there is a helper function `_apply_membership_multiplier` that is only used once inside the `calculate_loyalty_points` function. Your task is to inline this helper function's logic directly into where it's called and then remove the original helper function.

## Requirements
1. Move all the logic from `_apply_membership_multiplier` into `calculate_loyalty_points` where it is called
2. Preserve any comments from the helper function
3. Delete the original `_apply_membership_multiplier` function completely
4. Maintain the exact same functionality and calculations
5. Keep the same variable names from the helper function

The inlined code should replace the line that calls `_apply_membership_multiplier` and preserve the exact same logic and order of operations.