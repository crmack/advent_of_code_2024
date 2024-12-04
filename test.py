import unittest

from days import (
    day1, day2, day3
)

BASE_PATH = '/Users/chrismack/projects/learning/adventofcode/advent_of_code_2024/'

class TestAoC(unittest.TestCase):

    def test_day1(self):
        day1.run(BASE_PATH + '/inputs/day1.txt')
        day1.run_pd(BASE_PATH + '/inputs/day1.txt')

    def test_day2(self):
        day2.run(BASE_PATH + '/inputs/day2.txt')
        # day2.run_pd(BASE_PATH + '/inputs/day2_test.txt')

    def test_day3(self):
        day3.run(BASE_PATH + '/inputs/day3.txt')
        # day2.run_pd(BASE_PATH + '/inputs/day2_test.txt')


if __name__ == '__main__':
    unittest.main()