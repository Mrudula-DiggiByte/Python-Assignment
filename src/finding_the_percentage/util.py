def calculate_average_score(n, student_data, query_name):
    student_marks = {}
    for entry in student_data:
        name, *scores = entry.split()
        student_marks[name] = list(map(float, scores))

    scores = student_marks.get(query_name, [])
    if not scores:
        return "Student not found"

    average = sum(scores) / len(scores)
    return f"{average:.2f}"