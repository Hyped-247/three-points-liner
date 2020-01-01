def is_on_line(a: int, b: int, c: int, point: list):
    """
    :param a: int
    :param b: int
    :param c: int
    :param point: a list containing two integers
    :return: bool
    """
    return formula(a, b, point) * (point[1]) == c


def formula(a: int, b: int, point: list):
    """
    :param a: int
    :param b: int
    :param point: a list containing two integers
    :return: the value of
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
            if not isinstance(first_element, int) and not isinstance(second_element, int):
                raise TypeError("The points list must only contain numbers.")
            return point
        else:
            raise TypeError("Each list of points must contain two integers.")
    else:
        raise TypeError("Please input a list of points.")


def find_line_given_two_points(p: list, q: list):
    """
    :param p: int
    :param q: int
    :return: values for two given points.
    """
    a = q[1] - p[1]
    b = p[0] - q[0]
    c = formula(a, b, p)
    return a, b, c
