import unittest
from lines_finder.lines_finder import LinesFinder
from point.point import Point


class TestLine(unittest.TestCase):

    def setUp(self):

        self.points_1 = [Point(1, 2), Point(1, 3), Point(1, 4), Point(1, 2)]
        self.lines_finder_obj_1 = LinesFinder(self.points_1)
        self.tuple_line_1 = [(True, 1.0, None)]
        self.str_line_1 = ['x = 1.0']
        self.dict_line_1 = [{'x': 1.0}]

        self.points_2 = [Point(1, 2), Point(1, 3), Point(1, 4),  # two lines
                         Point(1, 7), Point(2, 3), Point(5, 9), Point(0, -1)]
        self.lines_finder_obj_2 = LinesFinder(self.points_2)
        self.tuple_line_2 = [(False, 2.0, -1.0), (True, 1.0, None)]
        self.str_line_2 = ['y = 2.0x + -1.0', 'x = 1.0']
        self.dict_line_2 = [{'y': 2.0, 'x': -1.0}, {'x': 1.0}]

    def test_get_line_tuple(self):
        tuple_lines = [res.get_line_tuple() for res in
                       self.lines_finder_obj_1.get_lines_intersect_three_or_more_points()]
        self.assertEqual(tuple_lines, self.tuple_line_1)

        tuple_lines = [res.get_line_tuple() for res in
                       self.lines_finder_obj_2.get_lines_intersect_three_or_more_points()]
        self.assertEqual(tuple_lines, self.tuple_line_2)

    def test_get_line_dict(self):
        dict_lines = [res.get_line_dict() for res in
                      self.lines_finder_obj_1.get_lines_intersect_three_or_more_points()]
        self.assertEqual(dict_lines, self.dict_line_1)

        dict_lines = [res.get_line_dict() for res in
                      self.lines_finder_obj_2.get_lines_intersect_three_or_more_points()]
        self.assertEqual(dict_lines, self.dict_line_2)

    def test_get_line_str(self):
        str_lines = [res.get_line_str() for res in
                     self.lines_finder_obj_1.get_lines_intersect_three_or_more_points()]
        self.assertEqual(str_lines, self.str_line_1)

        str_lines = [res.get_line_str() for res in
                     self.lines_finder_obj_2.get_lines_intersect_three_or_more_points()]
        self.assertEqual(str_lines, self.str_line_2)

    def tearDown(self):
        self.points_1 = None
        self.points_2 = None


if __name__ == '__main__':
    unittest.main()