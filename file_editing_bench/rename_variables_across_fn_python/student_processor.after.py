def calculate_final_score(scores):
    hw_scores = get_homework_scores(scores)
    exam_scores = get_exam_scores(scores)
    
    total = sum(hw_scores) * 0.4 + sum(exam_scores) * 0.6
    return round(total, 2)

def get_homework_scores(scores):
    return [score for score in scores if score < 100]

def get_exam_scores(scores):
    return [score for score in scores if score >= 100]

def generate_report(scores):
    hw = get_homework_scores(scores)
    exams = get_exam_scores(scores)
    
    report = {
        'homework_avg': sum(hw) / len(hw) if hw else 0,
        'exam_avg': sum(exams) / len(exams) if exams else 0,
        'final_score': calculate_final_score(scores)
    }
    return report

def process_class_data(all_scores):
    return [generate_report(scores) for scores in all_scores]