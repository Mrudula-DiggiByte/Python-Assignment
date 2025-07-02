from src.finding_the_percentage.util import calculate_average_score

n = int(input("Enter number of students: "))
student_data = [input(f"Enter name and scores for student {i + 1}: ") for i in range(n)]
query_name = input("Enter the name of student to query: ")

result = calculate_average_score(n, student_data, query_name)
print(result)