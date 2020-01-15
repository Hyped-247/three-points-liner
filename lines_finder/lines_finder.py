from line.line import Line
from itertools import combinations


class LinesFinder:
    """
    This class is responsible for finding lines given a list of point objects.
    """
    def __init__(self, points: list):
        """
        :param points: a list containing Point objects (ex. [Point(1, 2), Point(1, 3), Point(1, 4)])
        :return nothing
        """
        self._points = set(points)
        self._result = set()

    def get_lines_intersect_three_or_more_points(self):
        """
        Uses a list containing Point objects (ex. [Point(1, 2), Point(1, 3), Point(1, 4)]),
        and returns a list of Line objects that intersect with three or more points.
        :return: a list of Line objects.
        """

        points_len = len(self._points)
        if points_len <= 2:
            return []

        perm = list(combinations(self._points, 3))

        for element in perm:
            point_1, point_2, point_3 = element[0], element[1], element[2]

            line = Line(point_1, point_2, point_3)

            if line.get_line_tuple():
                self._result.add(line)  # add a line object

        return list(self._result)

