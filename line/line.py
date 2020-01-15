from point.point import Point


class Line:
    """
    Computes, validates, and formats line objects.
    """
    def __init__(self, p1: Point, p2: Point, p3: Point):
        """
        :param p1: Point
        :param p2: Point
        :param p3: Point
        """
        self._p1 = p1
        self._p2 = p2
        self._p3 = p3
        self._line = self._collinear()

    def _collinear(self) -> tuple or None:
        """
        Finds the collinear given three points.
        :return: a tuple of line (if three points on the same line) or None
        """
        x1, y1, x2, y2, x3, y3 = self._p1.get_x(), self._p1.get_y(), self._p2.get_x(), \
                                 self._p2.get_y(), self._p3.get_x(), self._p3.get_y()
        if (y3 - y2) * (x2 - x1) == (y2 - y1) * (x3 - x2):
            return self._compute_line([x1, y1], [x2, y2])

        return None

    def _compute_line(self, p1: list, p2: list) -> tuple:
        """
        Computes the line and returns it.
        :param p1: list of two numbers
        :param p2: list of two numbers
        :return: a line as a tuple of (bool, m, c)
        """
        a, b, c = self._find_line_given_two_points(p1, p2)

        if b == 0:
            return True, c / a, None

        return False, -1 * a / b, c / b

    def _find_line_given_two_points(self, p: list, q: list) -> tuple:
        """
        Finds a line given two points.
        :param p: list
        :param q: list
        :return: line which passes through two points
        """
        a = q[1] - p[1]
        b = p[0] - q[0]
        c = self._get_slope_value(a, b, p)
        return a, b, c

    @staticmethod
    def _get_slope_value(a: int, b: int, point: list) -> int or float:
        """
        Finds the slope.
        :param a: number
        :param b: number
        :param point: a list containing two numbers
        :return: value of the slope
        """
        return (a * (point[0])) + (b * (point[1]))

    def get_line_str(self) -> str:
        """
        Format a line.
        :return: str
        """
        if self._line[0]:
            return f"x = {self._line[1]}"

        return f"y = {self._line[1]}x + {self._line[2]}"

    def get_line_tuple(self):
        """
        :return: a line as a tuple of (bool, m, c) or None.
        """
        return self._line

    def get_line_dict(self):
        """
        :return: dict
        """
        if self._line[0]:
            return {'x': self._line[1]}

        return {'y': self._line[1], 'x': self._line[2]}

    def __eq__(self, other):
        """
        :param other:
        :return: bool
        """
        return self.get_line_tuple() == other.get_line_tuple()

    def __hash__(self):
        """
        :return: int
        """
        return hash(self.get_line_tuple())
