import unittest
from utilities.validator import validate_list_point, validate_has_duplicates, validate_three_points


class ValidatorTest(unittest.TestCase):

    def setUp(self):
        self.single_element = [8]
        self.bool = [True]
        self.wrong_type = [['1', 3]]
        self.duplicate_points = [[1, 2], [1, 2], [1, 3]]
        self.no_duplicate_points = [[1, 5], [1, 2], [1, 3]]
        self.no_duplicate_points_tuple = ([1, 5], [1, 2], [1, 3])

    def test_validate_has_duplicates(self):
        self.assertTrue(validate_has_duplicates(self.duplicate_points), True)
        self.assertFalse(validate_has_duplicates(self.no_duplicate_points), False)

    def test_validate_list_point(self):
        with self.assertRaises(TypeError):
            self.assertEqual(validate_list_point(self.bool), 1)
            self.assertEqual(validate_list_point(self.single_element), 1)
            self.assertEqual(validate_list_point(self.wrong_type), 1)

    def test_validate_three_points(self):
        self.assertEqual(validate_three_points(self.no_duplicate_points[0], self.no_duplicate_points[1],
                                               self.no_duplicate_points[2]),  self.no_duplicate_points_tuple)


if __name__ == '__main__':
    unittest.main()