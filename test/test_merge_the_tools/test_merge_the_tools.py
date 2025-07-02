import unittest
from src.merge_the_tools.util import merge_the_tools
import io
import sys

class TestMergeTheTools(unittest.TestCase):

    def test_basic_case(self):
        string = "AABCAAADA"
        k = 3
        expected_output = "AB\nCA\nAD\n"

        captured_output = io.StringIO()
        sys.stdout = captured_output

        merge_the_tools(string, k)

        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_no_duplicates(self):
        string = "ABCDE"
        k = 1
        expected_output = "A\nB\nC\nD\nE\n"

        captured_output = io.StringIO()
        sys.stdout = captured_output

        merge_the_tools(string, k)

        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_all_duplicates(self):
        string = "AAAAAA"
        k = 2
        expected_output = "A\nA\nA\n"

        captured_output = io.StringIO()
        sys.stdout = captured_output

        merge_the_tools(string, k)

        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
