def load_student_data(lst):
    students = []
    for student in lst:
        if isinstance(student, dict):
            students.append({
                'name': student.get('name'),
                'score': student.get('score', 0),
                'grade': calculate_grade(student.get('score', 0))
            })
    return students

def calculate_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

def get_class_statistics(students):
    if not students:
        return None
    
    total = 0
    count = len(students)
    
    for student in students:
        total += student.get('score', 0)
    
    avg = total / count if count > 0 else 0
    return {
        'average': avg,
        'total_students': count,
        'passing_rate': calculate_passing_rate(students)
    }

def calculate_passing_rate(students):
    if not students:
        return 0.0
    
    passing = 0
    for student in students:
        if student.get('score', 0) >= 60:
            passing += 1
    
    return (passing / len(students)) * 100