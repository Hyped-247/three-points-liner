import unittest
from lines_finder.lines_finder import LinesFinder
from point.point import Point


class LinesFinderTest(unittest.TestCase):

    def setUp(self):
        self.empty = []  # no lines.

        self.no_line = [Point(5, 9), Point(6, 8), Point(3, 5)]  # no lines.

        self.one_line = [Point(1, 2), Point(1, 3), Point(1, 4)]  # one line.

        self.two_lines = [Point(1, 2), Point(1, 3), Point(1, 4),  # two lines 
                          Point(1, 7),  Point(2, 3), Point(5, 9), Point(0, -1)]
        
        self.three_lines = [Point(1, 2,), Point(1, 3), Point(1, 4), Point(1, 7),  # three lines.
                            Point(2, 3), Point(5, 9), Point(0, -1), Point(0.5, 0),
                            Point(1, 1), Point(10, 10), Point(-4, -4)]

        self.four_lines = [Point(1, 2), Point(1, 3), Point(1, 4), Point(1, 7),  # four lines.
                           Point(2, 3), Point(5, 9), Point(0, -1), Point(0.5, 0),
                           Point(1, 1), Point(3, 3), Point(-4, -4)]

    @staticmethod
    def get_lines_intersect_three_or_more_points(points):
        return LinesFinder(points=points).get_lines_intersect_three_or_more_points()

    def test_less_than_three_points(self):
        line_objects = self.get_lines_intersect_three_or_more_points(self.empty)
        list_tuple_lines = [res.get_line_tuple() for res in line_objects]
        self.assertEqual(list_tuple_lines, [])

    def test_no_line(self):
        line_objects = self.get_lines_intersect_three_or_more_points(self.no_line)
        list_tuple_lines = [res.get_line_tuple() for res in line_objects]
        self.assertEqual(list_tuple_lines, [])

    def test_one_line(self):
        line_objects = self.get_lines_intersect_three_or_more_points(self.one_line)
        list_tuple_lines = [res.get_line_tuple() for res in line_objects]
        self.assertEqual(list_tuple_lines, [(True, 1.0, None)])

    def test_two_lines(self):
        line_objects = self.get_lines_intersect_three_or_more_points(self.two_lines)
        list_tuple_lines = [res.get_line_tuple() for res in line_objects]
        self.assertEqual(list_tuple_lines, [(False, 2.0, -1.0), (True, 1.0, None)])

    def test_three_lines(self):
        line_objects = self.get_lines_intersect_three_or_more_points(self.three_lines)
        list_tuple_lines = [res.get_line_tuple() for res in line_objects]
        self.assertEqual(list_tuple_lines, [(False, 1.0, 0.0), (False, 2.0, -1.0), (True, 1.0, None)])

    def test_four_lines(self):
        line_objects = self.get_lines_intersect_three_or_more_points(self.four_lines)
        list_tuple_lines = [res.get_line_tuple() for res in line_objects]
        self.assertEqual(list_tuple_lines, [(False, 1.0, 0.0), (False, 2.0, -1.0),
                                            (False, -0.0, 3.0), (True, 1.0, None)])


if __name__ == '__main__':
    unittest.main()