from typing import List, Dict
from datetime import datetime


def calculate_win_percentage(wins: int, total_games: int) -> float:
    """
    Calculate win percentage from wins and total games.
    Returns percentage between 0 and 100, rounded to 1 decimal place.
    """
    return round((wins / total_games * 100) if total_games > 0 else 0.0, 1)


def analyze_team_performance(game_results: List[Dict]) -> Dict:
    """Analyzes team performance from a list of game results."""
    total_points = 0
    total_games = len(game_results)
    wins = 0
    losses = 0
    points_by_quarter = {1: 0, 2: 0, 3: 0, 4: 0}
    
    for game in game_results:
        # Calculate total points
        team_score = game['team_score']
        opponent_score = game['opponent_score']
        total_points += team_score
        
        # Track wins/losses
        if team_score > opponent_score:
            wins += 1
        else:
            losses += 1
            
        # Add quarter-by-quarter points
        for quarter, points in game['quarter_points'].items():
            points_by_quarter[quarter] += points
    
    return {
        'total_games': total_games,
        'total_points': total_points,
        'wins': wins,
        'losses': losses,
        'win_percentage': calculate_win_percentage(wins, total_games),
        'avg_points_per_game': round(total_points / total_games, 1) if total_games > 0 else 0,
        'points_by_quarter': points_by_quarter
    }


if __name__ == "__main__":
    sample_games = [
        {
            'date': datetime(2023, 1, 1),
            'team_score': 98,
            'opponent_score': 88,
            'quarter_points': {1: 25, 2: 23, 3: 28, 4: 22}
        },
        {
            'date': datetime(2023, 1, 3),
            'team_score': 102,
            'opponent_score': 105,
            'quarter_points': {1: 28, 2: 24, 3: 22, 4: 28}
        }
    ]
    
    stats = analyze_team_performance(sample_games)
    print(stats)