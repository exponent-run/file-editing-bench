# Variable Renaming Task

In the file `order_processor.rb`, there is a variable `d` (both as instance variable `@d` and local variable `d`) that is used across multiple functions to track discounts. This variable name is not descriptive enough.

Your task is to rename all instances of this variable (both the instance variable `@d` and the local variable `d`) to `discount_amount` to better reflect its purpose and improve code readability.

Make sure to:
1. Rename the instance variable `@d` to `@discount_amount`
2. Rename all local variables `d` to `discount_amount`
3. Maintain the exact same functionality while only changing the variable names