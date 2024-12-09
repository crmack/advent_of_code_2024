import unittest

from days import (
    day1, day2, day3, day4, day5, day6, day7,
    day8, day9
)

BASE_PATH = '/Users/chrismack/projects/learning/adventofcode/advent_of_code_2024/'

class TestAoC(unittest.TestCase):

    def test_day1(self):
        day1.run(BASE_PATH + '/inputs/day1.txt')
        day1.run_pd(BASE_PATH + '/inputs/day1.txt')

    def test_day2(self):
        day2.run(BASE_PATH + '/inputs/day2.txt')

    def test_day3(self):
        day3.run(BASE_PATH + '/inputs/day3.txt')

    def test_day4(self):
        day4.run(BASE_PATH + '/inputs/day4.txt')

    def test_day5(self):
        day5.run(BASE_PATH + '/inputs/day5.txt')

    def test_day6(self):
        day6.run(BASE_PATH + '/inputs/day6.txt')

    def test_day7(self):
        day7.run(BASE_PATH + '/inputs/day7.txt')

    def test_day8(self):
        day8.run(BASE_PATH + '/inputs/day8.txt')

    def test_day9(self):
        day9.run(BASE_PATH + '/inputs/day9.txt')


if __name__ == '__main__':
    unittest.main()