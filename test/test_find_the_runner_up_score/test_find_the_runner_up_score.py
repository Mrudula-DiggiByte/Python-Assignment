import unittest
from src.find_the_runner_up_score.util import find_runner_up_score

class TestFindRunnerUpScore(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(find_runner_up_score(5, [2, 3, 6, 6, 5]), 5)

    def test_all_same_scores(self):
        self.assertEqual(find_runner_up_score(4, [7, 7, 7, 7]), "No runner-up")

    def test_two_scores_only(self):
        self.assertEqual(find_runner_up_score(2, [1, 1]), "No runner-up")

    def test_with_negatives(self):
        self.assertEqual(find_runner_up_score(5, [-5, -10, -2, -5, -1]), -2)

    def test_runner_up_is_negative(self):
        self.assertEqual(find_runner_up_score(3, [-5, -10, -5]), -10)

    def test_just_one_score(self):
        self.assertEqual(find_runner_up_score(1, [99]), "No runner-up")

    def test_with_duplicates(self):
        self.assertEqual(find_runner_up_score(6, [3, 3, 5, 5, 6, 6]), 5)

if __name__ == '__main__':
    unittest.main()
