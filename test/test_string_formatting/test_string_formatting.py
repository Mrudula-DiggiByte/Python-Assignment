import unittest
from io import StringIO
import sys
from src.string_formatting.util import print_formatted

class TestPrintFormatted(unittest.TestCase):

    def test_formatting_5(self):
        expected_output = (
            "    1     1     1     1\n"
            "    2     2     2    10\n"
            "    3     3     3    11\n"
            "    4     4     4   100\n"
            "    5     5     5   101\n"
        )

        captured_output = StringIO()
        sys.stdout = captured_output  # Redirect stdout
        print_formatted(5)
        sys.stdout = sys.__stdout__  # Reset stdout

        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_formatting_1(self):
        expected_output = "1 1 1 1\n"

        captured_output = StringIO()
        sys.stdout = captured_output
        print_formatted(1)
        sys.stdout = sys.__stdout__

        self.assertEqual(captured_output.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
