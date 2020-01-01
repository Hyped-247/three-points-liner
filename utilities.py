def collinear(x1, y1, x2, y2, x3, y3):
    """
    :param x1: int
    :param y1: int
    :param x2: int
    :param y2: int
    :param x3: int
    :param y3: int
    :return: tuple of dictionary lines or tuple of Nones
    """
    if (y3 - y2) * (x2 - x1) == (y2 - y1) * (x3 - x2):
        a, b, c = find_line_given_two_points([x1, y1], [x2, y2])
        line = {'a': a, 'b': b, 'c': c, "formatted_line": format_line(a, b, c)}

        a, b, c = find_line_given_two_points([x2, y2], [x3, y3])
        line2 = {'a': a, 'b': b, 'c': c, "formatted_line": format_line(a, b, c)}

        a, b, c = find_line_given_two_points([x1, y1], [x3, y3])
        line3 = {'a': a, 'b': b, 'c': c, "formatted_line": format_line(a, b, c)}

        return line, line2, line3

    return None, None, None


def get_slope_value(a: int, b: int, point: list):
    """
    :param a: int
    :param b: int
    :param point: a list containing two integers
    :return: value of the slope
    """
    return (a * (point[0])) + (b * (point[1]))


def validate(point: list):
    """
    :param point: a list containing two integers
    :return: validated point
    :raise TypeError
    """
    if isinstance(point, list):
        if len(point) == 2:
            first_element = point[0]
            second_element = point[1]
            if not isinstance(first_element, (int, float)) or not isinstance(second_element, (int, float)):
                raise TypeError("The points list must only contain float.")
            return point
        else:
            raise TypeError("Each list of points must contain two integers.")
    else:
        raise TypeError("Please input a list of points.")


def format_line(a, b, c):
    """
    :param a:
    :param b:
    :param c:
    :return:
    """
    if b < 0:
        return f"{a}x {b}y = {c}"
    return f"{a}x + {b}y = {c}"


def find_line_given_two_points(p: list, q: list):
    """
    :param p: int
    :param q: int
    :return: the equation of the line which passes through two points
    """
    a = q[1] - p[1]
    b = p[0] - q[0]
    c = get_slope_value(a, b, p)
    return a, b, c
