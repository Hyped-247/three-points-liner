import unittest
from point.point import Point


class TestPoint(unittest.TestCase):

    def setUp(self):
        self._point = Point(2, 7)

    def test_x(self):
        self.assertEqual(self._point.get_x(), 2)

    def test_y(self):
        self.assertEqual(self._point.get_y(), 7)

    def test_get_point(self):
        self.assertEqual(self._point.get_point(), (2, 7))

    def test_invalid_point(self):
        with self.assertRaises(TypeError):
            Point(1, '2')

    def tearDown(self):
        self._point = None


if __name__ == '__main__':
    unittest.main()