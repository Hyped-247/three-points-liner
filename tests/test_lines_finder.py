import unittest
from lines_finder import get_lines_intersect_three_or_more_points


class LinesFinderTest(unittest.TestCase):

    def setUp(self):
        self.list_1 = []
        self.list_2 = [[8], [1, 2], [8]]
        self.list_3 = [True, [1, 2], [2, 3]]
        self.list_4 = [[1, 2], [2, 4]]
        self.list_5 = [[1, 2], [2, 4], ['1', 3]]
        self.list_6 = [[], [], [], []]
        self.list_7 = [[5, 9], [6, 8], [3, 5]]  # no lines.
        self.list_8 = [[5, 9], [1, 1], [1, 1]]  # 2 lines.
        self.list_9 = [[1, 1], [5, 9], [2, 3]]  # 3 lines.

    def tearDown(self):
        self.list_1 = None
        self.list_2 = None
        self.list_3 = None
        self.list_4 = None
        self.list_5 = None
        self.list_6 = None
        self.list_7 = None
        self.list_8 = None
        self.list_9 = None

    def test_empty_list_points(self):
        self.assertEqual(get_lines_intersect_three_or_more_points(self.list_1), self.list_1)

    def test_incorrect_elements_number(self):
        with self.assertRaises(TypeError):
            self.assertEqual(get_lines_intersect_three_or_more_points(self.list_2), 2)

    def test_elements_type(self):
        with self.assertRaises(TypeError):
            self.assertEqual(get_lines_intersect_three_or_more_points(self.list_3), 2)

    def test_less_than_three_input(self):
        self.assertEqual(get_lines_intersect_three_or_more_points(self.list_4), self.list_1)

    def test_incorrect_elements_type(self):
        with self.assertRaises(TypeError):
            self.assertEqual(get_lines_intersect_three_or_more_points(self.list_5), self.list_5)

    def test_empty_lists(self):
        with self.assertRaises(TypeError):
            self.assertEqual(get_lines_intersect_three_or_more_points(self.list_6), self.list_6)

    def test_no_line(self):
        self.assertEqual(get_lines_intersect_three_or_more_points(self.list_7), self.list_1)

    def test_two_lines(self):
        line_1 = get_lines_intersect_three_or_more_points(self.list_8)[0]
        line_2 = get_lines_intersect_three_or_more_points(self.list_8)[1]

        expected_result_line_1 = {'a': -8, 'b': 4, 'c': -4}
        expected_result_line_2 = {'a': 0, 'b': 0, 'c': 0}

        self.assertEqual(line_1.get('a'), expected_result_line_1.get('a'))
        self.assertEqual(line_1.get('b'), expected_result_line_1.get('b'))
        self.assertEqual(line_1.get('c'), expected_result_line_1.get('c'))

        self.assertEqual(line_2.get('a'), expected_result_line_2.get('a'))
        self.assertEqual(line_2.get('b'), expected_result_line_2.get('b'))
        self.assertEqual(line_2.get('c'), expected_result_line_2.get('c'))

    def test_three_lines(self):
        line_1 = get_lines_intersect_three_or_more_points(self.list_9)[0]
        line_2 = get_lines_intersect_three_or_more_points(self.list_9)[1]
        line_3 = get_lines_intersect_three_or_more_points(self.list_9)[2]

        expected_result_line_1 = {'a': 8, 'b': -4, 'c': 4}
        expected_result_line_2 = {'a': -6, 'b': 3, 'c': -3}
        expected_result_line_3 = {'a': 2, 'b': -1, 'c': 1}

        self.assertEqual(line_1.get('a'), expected_result_line_1.get('a'))
        self.assertEqual(line_1.get('b'), expected_result_line_1.get('b'))
        self.assertEqual(line_1.get('c'), expected_result_line_1.get('c'))

        self.assertEqual(line_2.get('a'), expected_result_line_2.get('a'))
        self.assertEqual(line_2.get('b'), expected_result_line_2.get('b'))
        self.assertEqual(line_2.get('c'), expected_result_line_2.get('c'))

        self.assertEqual(line_3.get('a'), expected_result_line_3.get('a'))
        self.assertEqual(line_3.get('b'), expected_result_line_3.get('b'))
        self.assertEqual(line_3.get('c'), expected_result_line_3.get('c'))


if __name__ == '__main__':
    unittest.main()