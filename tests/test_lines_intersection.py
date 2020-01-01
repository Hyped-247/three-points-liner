import unittest
from lines_intersection import lines_intersection


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
        self.list_9 = ""  # 2 lines.

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
        self.assertEqual(lines_intersection(self.list_1), self.list_1)

    def test_incorrect_elements_number(self):
        with self.assertRaises(TypeError):
            self.assertEqual(lines_intersection(self.list_2), 2)

    def test_elements_type(self):
        with self.assertRaises(TypeError):
            self.assertEqual(lines_intersection(self.list_3), 2)

    def test_less_than_three_input(self):
        self.assertEqual(lines_intersection(self.list_4), self.list_1)

    def test_incorrect_elements_type(self):
        with self.assertRaises(TypeError):
            self.assertEqual(lines_intersection(self.list_5), self.list_5)

    def test_empty_lists(self):
        with self.assertRaises(TypeError):
            self.assertEqual(lines_intersection(self.list_6), self.list_6)

    def test_no_line(self):
        self.assertEqual(lines_intersection(self.list_7), self.list_1)

    # def test_one_line(self):
    #     line = lines_intersection(self.list_8)[0]
    #     self.assertEqual(line.a, "")
    #     self.assertEqual(line.b, "")
    #     self.assertEqual(line.c, "")
    #
    # def test_two_lines(self):
    #     line_1 = lines_intersection(self.list_9)[0]
    #     line_2 = lines_intersection(self.list_9)[1]
    #
    #     self.assertEqual(line_1.a, "")
    #     self.assertEqual(line_1.b, "")
    #     self.assertEqual(line_1.c, "")
    #
    #     self.assertEqual(line_2.a, "")
    #     self.assertEqual(line_2.b, "")
    #     self.assertEqual(line_2.c, "")


if __name__ == '__main__':
    unittest.main()