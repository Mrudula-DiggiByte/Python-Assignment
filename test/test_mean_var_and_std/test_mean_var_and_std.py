import unittest
import numpy as np
from src.mean_var_and_std.util import process_matrix_stats

class TestProcessMatrixStats(unittest.TestCase):

    def test_basic_2x3_matrix(self):
        array = np.array([
            [1, 2, 3],
            [4, 5, 6]
        ])

        mean, var, std = process_matrix_stats(array)

        expected_mean = np.array([2.0, 5.0])
        expected_var = np.array([2.25, 2.25, 2.25])
        expected_std = round(np.std(array), 11)

        np.testing.assert_array_almost_equal(mean, expected_mean)
        np.testing.assert_array_almost_equal(var, expected_var)
        self.assertEqual(std, expected_std)

    def test_single_row(self):
        array = np.array([[10, 20, 30]])
        mean, var, std = process_matrix_stats(array)

        expected_mean = np.array([20.0])
        expected_var = np.array([0.0, 0.0, 0.0])
        expected_std = round(np.std(array), 11)

        np.testing.assert_array_equal(mean, expected_mean)
        np.testing.assert_array_equal(var, expected_var)
        self.assertEqual(std, expected_std)

    def test_single_column(self):
        array = np.array([[1], [2], [3]])
        mean, var, std = process_matrix_stats(array)

        expected_mean = np.array([1.0, 2.0, 3.0])
        expected_var = np.array([0.66666667])
        expected_std = round(np.std(array), 11)

        np.testing.assert_array_almost_equal(mean, expected_mean)
        np.testing.assert_array_almost_equal(var, expected_var)
        self.assertEqual(std, expected_std)

if __name__ == '__main__':
    unittest.main()
