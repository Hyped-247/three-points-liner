def collinear(x1, y1, x2, y2, x3, y3):
    """
    :param x1: number
    :param y1: number
    :param x2: number
    :param y2: number
    :param x3: number
    :param y3: number
    :return: tuple of dictionary lines or tuple of Nones
    """
    if (y3 - y2) * (x2 - x1) == (y2 - y1) * (x3 - x2):

        return get_line([x1, y1], [x2, y2])

    return None, None, None


def get_line(p1, p2):
    """
    :param p1: list of two numbers
    :param p2: list of two numbers
    :return: dict of line
    """

    # Todo: all I need is a, c to form the formula.
    a, b, c = find_line_given_two_points(p1, p2)
    return {'a': a, 'b': b, 'c': c, "formatted_line": format_line(a, b, c)}


def get_slope_value(a: int, b: int, point: list):
    """
    :param a: number
    :param b: number
    :param point: a list containing two numbers
    :return: value of the slope
    """
    return (a * (point[0])) + (b * (point[1]))


def validate(point: list):
    """
    :param point: a list containing two numbers
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


# def add_lines(line, line2, line3, result):
#     """
#     :param line: dict
#     :param line2: dict
#     :param line3: dict
#     :param result: dict
#     :return: None
#     """
#     if can_add_line(line, result):
#         result.append(line)
#
#     if can_add_line(line2, result):
#         result.append(line2)
#
#     if can_add_line(line3, result):
#         result.append(line3)
#
#     return None
#
#
# def can_add_line(line, result):
#     """
#     :param line: dict
#     :param result: dict
#     :return: bool
#     """
#     return line and line not in result


def format_line(a, b, c):
    """
    :param a: number
    :param b: number
    :param c: number
    :return: formatted line formula
    """
    if b < 0:
        return f"{a}x {b}y = {c}"
    return f"{a}x + {b}y = {c}"


def find_line_given_two_points(p: list, q: list):
    """
    :param p: int
    :param q: int
    :return: line which passes through two points
    """
    a = q[1] - p[1]
    b = p[0] - q[0]
    c = get_slope_value(a, b, p)
    return a, b, c


def validate_points(p1, p2, p3):
    """
    :param p1: list of two numbers
    :param p2: list of two numbers
    :param p3: list of two numbers
    :return: a tuple of three validated lists
    """
    return validate(p1), validate(p2), validate(p3)
