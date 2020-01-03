import unittest
from utilities.format import format_line_str


class FormatTest(unittest.TestCase):

    def setUp(self):
        self.format_line_str_1 = format_line_str((True, 1, 3))
        self.format_line_str_2 = format_line_str((False, 1, 3))

    def test_format_line_str(self):
        self.assertEqual(self.format_line_str_1, 'x = 1')
        self.assertEqual(self.format_line_str_2, 'y = 1x + 3')


if __name__ == '__main__':
    unittest.main()