from utilities.validator import validate_three_points, validate_has_duplicates
from utilities.format import format_line_str
from utilities.compute_line import collinear
from itertools import combinations


class LinesFinder:
    def __init__(self, points: list) -> None:
        self._points = points
        self._result = set()

    def get_lines_intersect_three_or_more_points(self):
        """
        Takes a list containing non duplicates lists of points (ex. [[5, 9], [6, 8], [3, 5]]),
        and returns a list of lines that intersect with three or more points.
        :return: a list of lines (ex. ['y = 2.0x + -1.0', 'x = 1.0', ...])
        :raise TypeError if input data is not a list of lists containing two numbers.
        """
        points_len = len(self._points)
        if points_len <= 2:
            return []

        if validate_has_duplicates(self._points):
            raise TypeError('Duplicate points are not allowed.')

        perm = list(combinations(self._points, 3))

        for element in perm:
            point_1_validated, point_2_validated, point_3_validated = validate_three_points(element[0],
                                                                                            element[1],
                                                                                            element[2])
            line = collinear(point_1_validated, point_2_validated, point_3_validated)

            if line:
                self._result.add(line)

        return [format_line_str(res) for res in self._result]

