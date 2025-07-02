import unittest
from src.collections_namedtuple.util import calculate_average_marks

class TestCollectionsNamedTuple(unittest.TestCase):

    def test_average_marks_basic(self):
        n = 3
        headers = ['ID', 'MARKS', 'NAME', 'CLASS']
        data_rows = [
            '1 98 Alice 10',
            '2 87 Bob 10',
            '3 92 Charlie 10'
        ]
        result = calculate_average_marks(n, headers, data_rows)
        self.assertEqual(result, 92.33)

    def test_all_same_marks(self):
        n = 2
        headers = ['ID', 'MARKS', 'NAME', 'CLASS']
        data_rows = [
            '4 80 Dan 12',
            '5 80 Eve 12'
        ]
        result = calculate_average_marks(n, headers, data_rows)
        self.assertEqual(result, 80.0)

    def test_decimal_marks(self):
        n = 2
        headers = ['ID', 'MARKS', 'NAME', 'CLASS']
        data_rows = [
            '10 99.5 Zack 11',
            '11 100.0 Ana 11'
        ]
        result = calculate_average_marks(n, headers, data_rows)
        self.assertEqual(result, 99.75)

if __name__ == '__main__':
    unittest.main()
