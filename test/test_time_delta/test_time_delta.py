import unittest
from src.time_delta.util import time_delta

class TestTimeDelta(unittest.TestCase):

    def test_same_moment(self):
        t1 = "Sun 10 May 2015 13:54:36 -0700"
        t2 = "Sun 10 May 2015 13:54:36 -0700"
        self.assertEqual(time_delta(t1, t2), "0")

    def test_known_difference(self):
        t1 = "Sun 10 May 2015 13:54:36 -0700"
        t2 = "Sun 10 May 2015 13:54:36 -0000"
        # Difference = 7 hours = 25200 seconds
        self.assertEqual(time_delta(t1, t2), "25200")

    def test_difference_with_seconds(self):
        t1 = "Sun 10 May 2015 13:54:36 -0000"
        t2 = "Sun 10 May 2015 13:54:00 -0000"
        self.assertEqual(time_delta(t1, t2), "36")

    def test_day_and_timezone_diff(self):
        t1 = "Sat 02 May 2015 19:54:36 +0530"
        t2 = "Fri 01 May 2015 13:54:36 -0000"
        self.assertEqual(time_delta(t1, t2), "88200")

    def test_cross_day_diff(self):
        t1 = "Sat 10 May 2014 13:54:36 -0000"
        t2 = "Fri 09 May 2014 13:54:36 -0000"
        self.assertEqual(time_delta(t1, t2), "86400")  # 1 day = 86400 seconds

if __name__ == '__main__':
    unittest.main()
