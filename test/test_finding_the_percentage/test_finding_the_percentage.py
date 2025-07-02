import unittest
from src.finding_the_percentage.util import calculate_average_score

class TestCalculateAverageScore(unittest.TestCase):

    def test_valid_student(self):
        n = 3
        student_data = [
            "Alice 80 90 100",
            "Bob 70 75 80",
            "Charlie 60 70 80"
        ]
        result = calculate_average_score(n, student_data, "Bob")
        self.assertEqual(result, "75.00")

    def test_student_not_found(self):
        n = 2
        student_data = [
            "Dan 60 65 70",
            "Eve 85 90 95"
        ]
        result = calculate_average_score(n, student_data, "Tom")
        self.assertEqual(result, "Student not found")

    def test_scores_with_decimals(self):
        n = 2
        student_data = [
            "Zack 99.5 98.0 100.0",
            "Luna 78.5 80.25 85.75"
        ]
        result = calculate_average_score(n, student_data, "Zack")
        self.assertEqual(result, "99.17")  # (99.5 + 98.0 + 100.0) / 3 = 99.166...

    def test_only_one_score(self):
        n = 1
        student_data = ["Max 88"]
        result = calculate_average_score(n, student_data, "Max")
        self.assertEqual(result, "88.00")

if __name__ == '__main__':
    unittest.main()
