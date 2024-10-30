def calculate_final_score(d):
    hw_scores = get_homework_scores(d)
    exam_scores = get_exam_scores(d)
    
    total = sum(hw_scores) * 0.4 + sum(exam_scores) * 0.6
    return round(total, 2)

def get_homework_scores(d):
    return [score for score in d if score < 100]

def get_exam_scores(d):
    return [score for score in d if score >= 100]

def generate_report(d):
    hw = get_homework_scores(d)
    exams = get_exam_scores(d)
    
    report = {
        'homework_avg': sum(hw) / len(hw) if hw else 0,
        'exam_avg': sum(exams) / len(exams) if exams else 0,
        'final_score': calculate_final_score(d)
    }
    return report

def process_class_data(all_d):
    return [generate_report(d) for d in all_d]