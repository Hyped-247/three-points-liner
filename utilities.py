def is_on_line(a: int, b: int, c: int, point: list):
    """
    :param a: int
    :param b: int
    :param c: int
    :param point: a list containing two integers
    :return: bool
    """
    return get_slope_value(a, b, point) == c  # get_slope_value(a, b, point) * (point[1]) == c


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
