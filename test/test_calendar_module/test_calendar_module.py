import unittest
from src.calendar_module.util import get_weekday_name


class TestCalendarUtil(unittest.TestCase):

    def test_known_dates(self):
        # 4th July 2024 is a Thursday
        self.assertEqual(get_weekday_name(7, 4, 2024), "THURSDAY")

        # 1st January 2000 is a Saturday
        self.assertEqual(get_weekday_name(1, 1, 2000), "SATURDAY")

        # 15th August 1947 is a Friday
        self.assertEqual(get_weekday_name(8, 15, 1947), "FRIDAY")

        # 29th Feb 2020 is a Saturday (Leap Year)
        self.assertEqual(get_weekday_name(2, 29, 2020), "SATURDAY")

    def test_edge_cases(self):
        # 31st December 1999 is a Friday
        self.assertEqual(get_weekday_name(12, 31, 1999), "FRIDAY")

        # 1st March 1900 is a Thursday (1900 is not leap year)
        self.assertEqual(get_weekday_name(3, 1, 1900), "THURSDAY")


if __name__ == '__main__':
    unittest.main()
