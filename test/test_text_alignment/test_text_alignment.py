import unittest
from io import StringIO
import sys
from src.text_alignment.util import print_h_pattern

class TestPrintHPattern(unittest.TestCase):

    def test_thickness_3(self):
        # Expected output manually constructed for thickness = 3
        expected_output = (
            "  H  \n"
            " HHH \n"
            "HHHHH\n"
            "  H   H  \n"
            "  H   H  \n"
            "  H   H  \n"
            "  H   H  \n"
            "  H   H  \n"
            "HHHHHHHHH\n"
            "  H   H  \n"
            "  H   H  \n"
            "  H   H  \n"
            "  H   H  \n"
            "  H   H  \n"
            "      HHH\n"
            "       H \n"
            "        H\n"
        )

        # Capture printed output
        captured_output = StringIO()
        sys.stdout = captured_output
        print_h_pattern(3)
        sys.stdout = sys.__stdout__

        self.assertEqual(captured_output.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
