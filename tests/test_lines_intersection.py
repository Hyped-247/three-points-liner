import unittest
from lines_intersection import lines_intersection


class LinesIntersectionTest(unittest.TestCase):

    def setUp(self):
        self.list_1 = []
        self.list_2 = [[8], [1, 2], [8]]
        self.list_3 = [True, [1, 2], [2, 3]]
        self.list_4 = [[1, 2], [2, 4]]
        self.list_5 = [[1, 2], [2, 4], ['1', 3]]

        # self.list_5 = [[], [], [], []]
        # self.list_6 = [[1, 2], [2, 4]]
        # self.list_7 = [[1, 2], [2, 4], [1, 5]]
        # self.list_8 = [[1, 2], [2, 4], [1, 5]]

        # TODO: 3 points ==> 1 line.
        # TODO: 5 points ==> 1 line.
        # TODO: 4 points ==> 2 lines.
        # TODO: 3 points ==> 0 lines.

        # TODO: check if every element within the elements is a list.
        # TODO: check if every list contains two elements.
        # TODO: check that these two are elements are ints.
        # TODO: check that these two are elements are ints.

    def tearDown(self):
        self.list_1 = None
        self.list_2 = None
        self.list_3 = None
        self.list_4 = None
        self.list_5 = None

    def test_empty_list_points(self):
        self.assertEqual(lines_intersection(self.list_1), self.list_1)

    def test_incorrect_elements_number(self):
        with self.assertRaises(Exception):
            self.assertEqual(lines_intersection(self.list_2), 2)

    def test_elements_type(self):
        with self.assertRaises(TypeError):
            self.assertEqual(lines_intersection(self.list_3), 2)

    def test_less_than_three_input(self):
        self.assertEqual(lines_intersection(self.list_4), self.list_1)

    def test_incorrect_elements_type(self):
        with self.assertRaises(TypeError):
            self.assertEqual(lines_intersection(self.list_5), self.list_5)


if __name__ == '__main__':
    unittest.main()