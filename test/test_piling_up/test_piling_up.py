import unittest
from src.piling_up.util import is_piling_possible

class TestPilingUp(unittest.TestCase):

    def test_possible_case(self):
        cubes = [4, 3, 2, 1, 3, 4]
        result = is_piling_possible(cubes)
        self.assertEqual(result, "Yes")

    def test_impossible_case(self):
        cubes = [1, 3, 2]
        result = is_piling_possible(cubes)
        self.assertEqual(result, "No")

    def test_strictly_decreasing(self):
        cubes = [6, 5, 4, 3, 2, 1]
        result = is_piling_possible(cubes)
        self.assertEqual(result, "Yes")

    def test_strictly_increasing(self):
        cubes = [1, 2, 3, 4, 5]
        result = is_piling_possible(cubes)
        self.assertEqual(result, "Yes")

    def test_equal_elements(self):
        cubes = [3, 3, 3, 3]
        result = is_piling_possible(cubes)
        self.assertEqual(result, "Yes")

    def test_single_element(self):
        cubes = [5]
        result = is_piling_possible(cubes)
        self.assertEqual(result, "Yes")

    def test_two_elements_valid(self):
        cubes = [5, 3]
        result = is_piling_possible(cubes)
        self.assertEqual(result, "Yes")

    def test_two_elements_invalid(self):
        cubes = [3, 5]
        result = is_piling_possible(cubes)
        self.assertEqual(result, "Yes")  # still valid: pick 5 → pick 3

if __name__ == '__main__':
    unittest.main()
