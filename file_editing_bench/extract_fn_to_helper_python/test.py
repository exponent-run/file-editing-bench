import pytest
from task_files.grade_processor import calculate_final_grades, calculate_homework_average


@pytest.fixture
def sample_homework_scores():
    return [
        {'score': 85, 'days_late': 0},  # 85 (no penalty)
        {'score': 92, 'days_late': 1},  # 87.4 (5% penalty)
        {'score': 78, 'days_late': 3},  # 66.3 (15% penalty)
        {'score': 35, 'days_late': 0},  # should be ignored (<40%)
    ]


@pytest.fixture
def sample_student_records():
    return [
        {
            'student_id': 'ST101',
            'homework_scores': [
                {'score': 85, 'days_late': 0},
                {'score': 92, 'days_late': 1},
                {'score': 78, 'days_late': 3}
            ],
            'exam_scores': [88, 92],
            'project_score': 90
        }
    ]


def test_calculate_homework_average(sample_homework_scores):
    """Test that homework average calculation handles scores and late penalties correctly"""
    avg = calculate_homework_average(sample_homework_scores)
    # Expected: (85 + 87.4 + 66.3) / 3 = 79.57
    assert round(avg, 1) == 79.6


def test_calculate_homework_average_all_invalid():
    """Test handling of all scores below threshold"""
    scores = [
        {'score': 35, 'days_late': 0},
        {'score': 25, 'days_late': 1}
    ]
    avg = calculate_homework_average(scores)
    assert avg == 0


def test_calculate_homework_average_empty():
    """Test handling of empty homework scores"""
    assert calculate_homework_average([]) == 0


def test_calculate_final_grades(sample_student_records):
    """Test that final grade calculation works with the extracted helper function"""
    grades = calculate_final_grades(sample_student_records)
    assert len(grades) == 1
    student_id, grade = grades[0]
    assert student_id == 'ST101'
    # Final grade should be:
    # Homework (79.6 * 0.4) + Exams ((88 + 92)/2 * 0.4) + Project (90 * 0.2)
    # = 31.84 + 36 + 18 = 85.84
    assert grade == 85.8


def test_calculate_final_grades_empty():
    """Test handling of empty student records"""
    assert calculate_final_grades([]) == []