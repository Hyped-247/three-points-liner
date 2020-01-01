import unittest
from three_or_more_lines_finder import three_or_more_lines_finder


class LinesIntersectionTest(unittest.TestCase):

    def setUp(self):
        self.list_1 = []
        self.list_2 = [[8], [1, 2], [8]]
        self.list_3 = [True, [1, 2], [2, 3]]
        self.list_4 = [[1, 2], [2, 4]]
        self.list_5 = [[1, 2], [2, 4], ['1', 3]]
        self.list_6 = [[], [], [], []]
        self.list_7 = [[5, 9], [6, 8], [3, 5]]  # no lines.
        self.list_8 = ""  # 1 lines.
        self.list_9 = [[5, 9], [1, 1], [1, 1]]  # 2 lines.

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
        self.assertEqual(three_or_more_lines_finder(self.list_1), self.list_1)

    def test_incorrect_elements_number(self):
        with self.assertRaises(TypeError):
            self.assertEqual(three_or_more_lines_finder(self.list_2), 2)

    def test_elements_type(self):
        with self.assertRaises(TypeError):
            self.assertEqual(three_or_more_lines_finder(self.list_3), 2)

    def test_less_than_three_input(self):
        self.assertEqual(three_or_more_lines_finder(self.list_4), self.list_1)

    def test_incorrect_elements_type(self):
        with self.assertRaises(TypeError):
            self.assertEqual(three_or_more_lines_finder(self.list_5), self.list_5)

    def test_empty_lists(self):
        with self.assertRaises(TypeError):
            self.assertEqual(three_or_more_lines_finder(self.list_6), self.list_6)

    def test_no_line(self):
        self.assertEqual(three_or_more_lines_finder(self.list_7), self.list_1)

    # def test_one_line(self):
    #     line = three_or_more_lines_finder(self.list_8)[0]
    #     self.assertEqual(line.a, "")
    #     self.assertEqual(line.b, "")
    #     self.assertEqual(line.c, "")
    #
    def test_two_lines(self):
        line_1 = three_or_more_lines_finder(self.list_9)[0]
        line_2 = three_or_more_lines_finder(self.list_9)[1]
        expected_result_line_1 = {'a': -8, 'b': 4, 'c': -4}
        expected_result_line_2 = {'a': 0, 'b': 0, 'c': 0}

        self.assertEqual(line_1.get('a'), expected_result_line_1.get('a'))
        self.assertEqual(line_1.get('b'), expected_result_line_1.get('b'))
        self.assertEqual(line_1.get('c'), expected_result_line_1.get('c'))

        self.assertEqual(line_2.get('a'), expected_result_line_2.get('a'))
        self.assertEqual(line_2.get('b'), expected_result_line_2.get('b'))
        self.assertEqual(line_2.get('c'), expected_result_line_2.get('c'))


if __name__ == '__main__':
    unittest.main()