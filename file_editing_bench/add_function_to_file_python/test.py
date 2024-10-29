import pytest
from task_files.game_stats import analyze_team_performance, calculate_win_percentage
from datetime import datetime


def test_calculate_win_percentage():
    """Test the helper function directly"""
    assert calculate_win_percentage(5, 10) == 50.0
    assert calculate_win_percentage(3, 7) == 42.9
    assert calculate_win_percentage(0, 5) == 0.0
    assert calculate_win_percentage(0, 0) == 0.0
    assert calculate_win_percentage(10, 10) == 100.0


def test_analyze_team_performance_with_games():
    """Test that the main function uses the helper function correctly"""
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
    assert stats['win_percentage'] == 50.0
    assert stats['wins'] == 1
    assert stats['total_games'] == 2


def test_analyze_team_performance_empty():
    """Test edge case with no games"""
    stats = analyze_team_performance([])
    assert stats['win_percentage'] == 0.0
    assert stats['wins'] == 0
    assert stats['total_games'] == 0