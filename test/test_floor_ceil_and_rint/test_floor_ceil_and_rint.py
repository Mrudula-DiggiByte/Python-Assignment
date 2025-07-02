import unittest
from src.floor_ceil_and_rint.util import process_array
import numpy as np
import io
import sys

class TestNumpyArrayProcessing(unittest.TestCase):

    def test_basic_case(self):
        arr = [1.2, 2.5, 3.7, -1.2, -2.5]

        # Expected outputs
        expected_floor = np.floor(arr)
        expected_ceil = np.ceil(arr)
        expected_rint = np.rint(arr)

        # Capture output
        captured_output = io.StringIO()
        sys.stdout = captured_output

        process_array(arr)

        sys.stdout = sys.__stdout__  # Reset stdout

        # Extract printed lines and parse to arrays
        output_lines = captured_output.getvalue().strip().split('\n')
        actual_floor = np.fromstring(output_lines[0].strip('[]'), sep=' ')
        actual_ceil = np.fromstring(output_lines[1].strip('[]'), sep=' ')
        actual_rint = np.fromstring(output_lines[2].strip('[]'), sep=' ')

        # Assert arrays are equal
        np.testing.assert_array_equal(actual_floor, expected_floor)
        np.testing.assert_array_equal(actual_ceil, expected_ceil)
        np.testing.assert_array_equal(actual_rint, expected_rint)

if __name__ == '__main__':
    unittest.main()
