import unittest
from src.linear_algebra.util import calculate_determinant

class TestCalculateDeterminant(unittest.TestCase):

    def test_2x2_matrix(self):
        matrix = [[1, 2], [3, 4]]
        result = calculate_determinant(matrix)
        self.assertEqual(result, -2.0)

    def test_3x3_matrix(self):
        matrix = [[6, 1, 1],
                  [4, -2, 5],
                  [2, 8, 7]]
        result = calculate_determinant(matrix)
        self.assertEqual(result, -306.0)

    def test_identity_matrix(self):
        matrix = [[1.0, 0.0], [0.0, 1.0]]
        result = calculate_determinant(matrix)
        self.assertEqual(result, 1.0)

    def test_zero_matrix(self):
        matrix = [[0.0, 0.0], [0.0, 0.0]]
        result = calculate_determinant(matrix)
        self.assertEqual(result, 0.0)

    def test_symmetric_matrix(self):
        matrix = [[2, 3], [3, 2]]
        result = calculate_determinant(matrix)
        self.assertEqual(result, -5.0)

if __name__ == '__main__':
    unittest.main()
