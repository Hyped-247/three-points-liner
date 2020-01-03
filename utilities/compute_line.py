
def collinear(p1: list, p2: list, p3: list) -> tuple or None:
    """
    Finds the collinear given three points.
    :param p1: list of two numbers
    :param p2: list of two numbers
    :param p3: list of two numbers
    :return: a tuple of line (if three points on the same line) or None
    """
    x1, y1, x2, y2, x3, y3 = p1[0], p1[1], p2[0], p2[1], p3[0], p3[1]
    if (y3 - y2) * (x2 - x1) == (y2 - y1) * (x3 - x2):
        return get_line([x1, y1], [x2, y2])

    return None


def get_line(p1: list, p2: list):
    """
    Computes the line and returns it.
    :param p1: list of two numbers
    :param p2: list of two numbers
    :return: a line as a tuple of (bool, m, c)
    """
    a, b, c = find_line_given_two_points(p1, p2)

    if b == 0:
        return True, c / a, None

    return False, -1 * a / b, c / b


def find_line_given_two_points(p: list, q: list) -> tuple:
    """
    Finds a line given two points.
    :param p: list
    :param q: list
    :return: line which passes through two points
    """
    a = q[1] - p[1]
    b = p[0] - q[0]
    c = get_slope_value(a, b, p)
    return a, b, c


def get_slope_value(a: int, b: int, point: list) -> int or float:
    """
    Finds the slope.
    :param a: number
    :param b: number
    :param point: a list containing two numbers
    :return: value of the slope
    """
    return (a * (point[0])) + (b * (point[1]))

