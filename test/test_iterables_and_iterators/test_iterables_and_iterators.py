import unittest
from src.iterables_and_iterators.util import calculate_a_ratio

class TestCalculateARatio(unittest.TestCase):

    def test_example_case(self):
        letters = ['a', 'b', 'c']
        k = 2
        result = calculate_a_ratio(letters, k)
        self.assertEqual(result, 0.667)  # Combinations: ab, ac, bc → 2 have 'a'

    def test_no_a_present(self):
        letters = ['b', 'c', 'd']
        k = 2
        result = calculate_a_ratio(letters, k)
        self.assertEqual(result, 0.000)  # No 'a'

    def test_all_combinations_have_a(self):
        letters = ['a', 'a', 'a']
        k = 2
        result = calculate_a_ratio(letters, k)
        self.assertEqual(result, 1.000)  # All combinations have 'a'

    def test_single_letter_a(self):
        letters = ['a']
        k = 1
        result = calculate_a_ratio(letters, k)
        self.assertEqual(result, 1.000)

    def test_single_letter_non_a(self):
        letters = ['x']
        k = 1
        result = calculate_a_ratio(letters, k)
        self.assertEqual(result, 0.000)

    def test_case_sensitive(self):
        letters = ['A', 'a']
        k = 1
        result = calculate_a_ratio(letters, k)
        self.assertEqual(result, 0.5)  # Only one lowercase 'a'

if __name__ == '__main__':
    unittest.main()
