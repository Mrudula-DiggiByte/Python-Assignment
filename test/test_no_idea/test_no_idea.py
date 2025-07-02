import unittest
from src.no_idea.util import calculate_happiness

class TestCalculateHappiness(unittest.TestCase):

    def test_basic_case(self):
        arr = [1, 5, 3]
        A = {3, 1}
        B = {5, 7}
        result = calculate_happiness(arr, A, B)
        self.assertEqual(result,1)  # +1 (1), -1 (5), +1 (3) → 1-1+1 = 1

    def test_all_liked(self):
        arr = [1, 2, 3]
        A = {1, 2, 3}
        B = set()
        result = calculate_happiness(arr, A, B)
        self.assertEqual(result, 3)

    def test_all_disliked(self):
        arr = [4, 5, 6]
        A = set()
        B = {4, 5, 6}
        result = calculate_happiness(arr, A, B)
        self.assertEqual(result, -3)

    def test_neutral_case(self):
        arr = [10, 20, 30]
        A = {1, 2}
        B = {3, 4}
        result = calculate_happiness(arr, A, B)
        self.assertEqual(result, 0)  # None match A or B

    def test_mixed_case(self):
        arr = [1, 2, 3, 4, 5]
        A = {1, 3, 5}
        B = {2, 4}
        result = calculate_happiness(arr, A, B)
        self.assertEqual(result, 1)  # +1 (1), -1 (2), +1 (3), -1 (4), +1 (5) → total = 1

if __name__ == '__main__':
    unittest.main()
