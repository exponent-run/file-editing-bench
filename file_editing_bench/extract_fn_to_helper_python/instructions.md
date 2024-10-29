# Extract Homework Average Calculation

The file `grade_processor.py` contains a function `calculate_final_grades` that processes student grades. The function contains complex logic for calculating homework averages that should be extracted into a helper function.

## Task

Extract the homework average calculation logic into a new helper function with these exact specifications:

1. Create a new function named `calculate_homework_average` that:
   - Takes a single parameter `homework_scores: List[Dict]`
   - Returns a float representing the homework average
   - Contains all the logic for:
     - Filtering out scores below 40%
     - Applying late penalties (5% per day up to 30%)
     - Calculating the average of valid scores

2. Modify the original `calculate_final_grades` function to:
   - Call the new `calculate_homework_average` function
   - Pass the homework scores to it
   - Use its return value in the final grade calculation

The extracted function should maintain the exact same logic and behavior as the original code.

## Example

The helper function should handle homework scores in this format:
```python
homework_scores = [
    {'score': 85, 'days_late': 0},
    {'score': 92, 'days_late': 1},
    {'score': 78, 'days_late': 3}
]
```

And should be called like this:
```python
homework_avg = calculate_homework_average(homework_scores)
```