import unittest
from utilities.compute_line import collinear, get_line, get_slope_value, find_line_given_two_points


class ComputeLineTest(unittest.TestCase):

    def setUp(self):
        self.no_duplicate_points = [[1, 5], [1, 2], [1, 3]]

    def test_collinear(self):
        result = collinear(self.no_duplicate_points[0], self.no_duplicate_points[1],
                           self.no_duplicate_points[2])
        self.assertEqual(result, (True, 1.0, None))

    def test_get_line(self):
        result = get_line(self.no_duplicate_points[0], self.no_duplicate_points[1])
        self.assertEqual(result, (True, 1.0, None))

    def test_find_line_given_two_points(self):
        result = find_line_given_two_points(self.no_duplicate_points[0],
                                            self.no_duplicate_points[1])
        self.assertEqual(result, (-3, 0, -3))

    def test_get_slope_value(self):
        result = get_slope_value(1, 2, self.no_duplicate_points[1])
        self.assertEqual(result, 5)


if __name__ == '__main__':
    unittest.main()