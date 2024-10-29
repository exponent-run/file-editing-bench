def load_student_data(lst):
    d = []
    for i in lst:
        if isinstance(i, dict):
            d.append({
                'name': i.get('name'),
                'score': i.get('score', 0),
                'grade': calculate_grade(i.get('score', 0))
            })
    return d

def calculate_grade(i):
    if i >= 90:
        return 'A'
    elif i >= 80:
        return 'B'
    elif i >= 70:
        return 'C'
    elif i >= 60:
        return 'D'
    else:
        return 'F'

def get_class_statistics(d):
    if not d:
        return None
    
    total = 0
    count = len(d)
    
    for i in d:
        total += i.get('score', 0)
    
    avg = total / count if count > 0 else 0
    return {
        'average': avg,
        'total_students': count,
        'passing_rate': calculate_passing_rate(d)
    }

def calculate_passing_rate(d):
    if not d:
        return 0.0
    
    passing = 0
    for i in d:
        if i.get('score', 0) >= 60:
            passing += 1
    
    return (passing / len(d)) * 100