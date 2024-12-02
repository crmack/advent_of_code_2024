import unittest

from days import (
    day1
)

BASE_PATH = '/Users/chrismack/projects/learning/adventofcode/advent_of_code_2024/'

class TestAoC(unittest.TestCase):

    def test_day1(self):
        day1.run(BASE_PATH + '/inputs/day1.txt')


if __name__ == '__main__':
    unittest.main()