# Add Helper Function for Win Percentage Calculation

Your task is to add a helper function called `calculate_win_percentage` to the file and refactor the main function to use it. The helper function should:

1. Be added to the file `game_stats.py`
2. Have the following exact signature:
   ```python
   def calculate_win_percentage(wins: int, total_games: int) -> float:
       """
       Calculate win percentage from wins and total games.
       Returns percentage between 0 and 100, rounded to 1 decimal place.
       """
   ```
3. Implement the win percentage calculation that's currently done inline in `analyze_team_performance`
4. Return 0.0 if total_games is 0
5. Round the result to 1 decimal place

Then modify the `analyze_team_performance` function to use this helper function instead of calculating the win percentage inline.

The helper function should be used to make the code more maintainable and reusable, while keeping the exact same behavior as before.