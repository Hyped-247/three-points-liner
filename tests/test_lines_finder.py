import unittest
from lines_finder import LinesFinder


class LinesFinderTest(unittest.TestCase):

    def setUp(self):
        self.list_1 = []
        self.list_2 = [[8], [1, 2], [8]]
        self.list_3 = [True, [1, 2], [2, 3]]
        self.list_4 = [[1, 2], [2, 4]]
        self.list_5 = [[1, 2], [2, 4], ['1', 3]]
        self.list_6 = [[], [], [], []]
        self.list_7 = [[5, 9], [6, 8], [3, 5]]  # no lines.
        self.list_8 = [[1, 2], [1, 3], [1, 4]]  # one line.
        self.list_9 = [[1, 2], [1, 3], [1, 4], [1, 7],  # two lines.
                       [2, 3], [5, 9], [0, -1]]
        self.list_10 = [[1, 2], [1, 3], [1, 4], [1, 7],  # three lines.
                        [2, 3], [5, 9], [0, -1], [0.5, 0],
                        [1, 1], [10, 10], [-4, -4]]
        self.list_11 = [[1, 2], [1, 3], [1, 4], [1, 7],  # four lines.
                        [2, 3], [5, 9], [0, -1], [0.5, 0],
                        [1, 1], [3, 3], [-4, -4]]
        self.list_12 = [[1, 2], [1, 2], [1, 3]]

    @staticmethod
    def get_lines_intersect_three_or_more_points(points):
        return LinesFinder(points=points).get_lines_intersect_three_or_more_points()

    def test_empty_list_points(self):
        self.assertEqual(self.get_lines_intersect_three_or_more_points(self.list_1), self.list_1)

    def test_incorrect_elements_number(self):
        with self.assertRaises(TypeError):
            self.assertEqual(self.get_lines_intersect_three_or_more_points(self.list_2), 2)

    def test_elements_type(self):
        with self.assertRaises(TypeError):
            self.assertEqual(self.get_lines_intersect_three_or_more_points(self.list_3), 2)

    def test_less_than_three_input(self):
        self.assertEqual(self.get_lines_intersect_three_or_more_points(self.list_4), self.list_1)

    def test_incorrect_elements_type(self):
        with self.assertRaises(TypeError):
            self.assertEqual(self.get_lines_intersect_three_or_more_points(self.list_5), self.list_5)

    def test_empty_lists(self):
        with self.assertRaises(TypeError):
            self.assertEqual(self.get_lines_intersect_three_or_more_points(self.list_6), self.list_6)

    def test_duplicate_points(self):
        with self.assertRaises(TypeError):
            self.assertEqual(self.get_lines_intersect_three_or_more_points(self.list_12), self.list_12)

    def test_no_line(self):
        self.assertEqual(self.get_lines_intersect_three_or_more_points(self.list_7), self.list_1)

    def test_one_line(self):
        result = set(self.get_lines_intersect_three_or_more_points(self.list_8))
        expected = {'x = 1.0'}
        self.assertEqual(result, expected)

    def test_two_lines(self):
        result = set(self.get_lines_intersect_three_or_more_points(self.list_9))
        expected = {'y = 2.0x + -1.0', 'x = 1.0'}
        self.assertEqual(result, expected)

    def test_three_lines(self):
        result = set(self.get_lines_intersect_three_or_more_points(self.list_10))
        expected = {'y = 1.0x + -0.0', 'y = 2.0x + -1.0', 'x = 1.0'}
        self.assertEqual(result, expected)

    def test_four_lines(self):
        result = set(self.get_lines_intersect_three_or_more_points(self.list_11))
        expected = {'y = 1.0x + -0.0',
                    'y = 2.0x + -1.0',
                    'y = -0.0x + 3.0',
                    'x = 1.0'}
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()