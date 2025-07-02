import unittest
from src.min_and_max.util import min_then_max

class TestMinThenMax(unittest.TestCase):

    def test_standard_matrix(self):
        data = [
            [2, 5],
            [3, 7],
            [1, 3],
            [4, 0]
        ]
        # Row mins: [2, 3, 1, 0] → max = 3
        self.assertEqual(min_then_max(data), 3)

    def test_all_same_values(self):
        data = [
            [1, 1],
            [1, 1]
        ]
        # Row mins: [1, 1] → max = 1
        self.assertEqual(min_then_max(data), 1)

    def test_negative_values(self):
        data = [
            [-5, -1],
            [-10, -2],
            [-3, -4]
        ]
        # Row mins: [-5, -10, -4] → max = -4
        self.assertEqual(min_then_max(data), -4)

    def test_single_row(self):
        data = [[10, 20, 30]]
        # Row mins: [10] → max = 10
        self.assertEqual(min_then_max(data), 10)

    def test_single_column(self):
        data = [[1], [5], [3]]
        # Row mins: [1, 5, 3] → max = 5
        self.assertEqual(min_then_max(data), 5)

if __name__ == '__main__':
    unittest.main()
