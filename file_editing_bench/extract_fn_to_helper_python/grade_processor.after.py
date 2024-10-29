from typing import List, Dict, Tuple
from datetime import datetime


def calculate_homework_average(homework_scores: List[Dict]) -> float:
    total_homework_score = 0
    valid_homework_count = 0
    for score in homework_scores:
        # Skip any homework below 40% as it was likely not a serious attempt
        if score >= 40:
            # Apply late penalty if submission was late
            if score.get('days_late', 0) > 0:
                penalty = min(score.get('days_late', 0) * 5, 30)  # 5% per day up to 30%
                adjusted_score = score['score'] * (100 - penalty) / 100
            else:
                adjusted_score = score['score']
            # Add to total and increment counter
            total_homework_score += adjusted_score
            valid_homework_count += 1
    
    return (total_homework_score / valid_homework_count) if valid_homework_count > 0 else 0


def calculate_final_grades(student_records: List[Dict]) -> List[Tuple[str, float]]:
    final_grades = []
    
    for record in student_records:
        # Get the student's raw scores and weights
        homework_scores = record.get('homework_scores', [])
        exam_scores = record.get('exam_scores', [])
        project_score = record.get('project_score', 0)
        
        # Calculate homework average using helper function
        homework_avg = calculate_homework_average(homework_scores)
        
        # Calculate exam average
        exam_avg = sum(exam_scores) / len(exam_scores) if exam_scores else 0
        
        # Calculate final grade with weights
        final_grade = (homework_avg * 0.4) + (exam_avg * 0.4) + (project_score * 0.2)
        
        # Round to nearest tenth
        final_grade = round(final_grade, 1)
        
        final_grades.append((record['student_id'], final_grade))
    
    return final_grades


if __name__ == "__main__":
    # Example usage
    students = [
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
    print(calculate_final_grades(students))