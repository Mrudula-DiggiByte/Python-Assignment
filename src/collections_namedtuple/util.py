from collections import namedtuple

def calculate_average_marks(n, headers, data_rows):
    Student = namedtuple('Student', headers)
    students = [Student(*row.split()) for row in data_rows]
    average = sum(float(student.MARKS) for student in students) / n
    return f"{average:.2f}"