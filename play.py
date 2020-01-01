from itertools import combinations


def format_line(tup):
    if tup[0]:  # m is inf. => vertical lines
        c = tup[1]
        return (tup[0], tup[1], tup[2], f"x = {c}")
    elif abs(tup[1]) < 0.00000000001:  # floating point equals
        c = tup[2]
        return (tup[0], tup[1], tup[2], f"y = {c}")
    else:
        m = tup[1]
        c = tup[2]
        return (tup[0], tup[1], tup[2], f"y = {m}x + {c}")


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
        # they are collinear.
        return get_line([x1, y1], [x2, y2])
    else:
        return None


def get_line(p1, p2):
    """
    :param p1: list of two numbers
    :param p2: list of two numbers
    :return: a line as a tuple of (m, c)
    """
    a, b, c = find_line_given_two_points(p1, p2)

    if b == 0:
        line = (True, c / a, None)  # equations of type x = c
    else:
        line = (False, -1 * a / b, c / b)  # line in y = mx + c / tuple of (is_m_inf, m, c)

    return line


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


def validate_points(p1, p2, p3):
    """
    :param p1: list of two numbers
    :param p2: list of two numbers
    :param p3: list of two numbers
    :return: a tuple of three validated lists
    """
    return validate(p1), validate(p2), validate(p3)


def get_lines_intersect_three_or_more_points(points):
    """
    :param points: a list containing lists of points (ex. [[5, 9], [6, 8], [3, 5]])
    :return: a list of dictionaries (ex.[{'a': -8, 'b': 4, 'c': -4, 'formatted_line': '-8x + 4y = -4'}, ...]).
    :raise TypeError  ???
    """
    list_points_len = len(points)
    if list_points_len <= 2:
        return []

    result = set()
    perm = list(combinations(points, 3))

    for element in perm:
        point_1_validated, point_2_validated, point_3_validated = validate_points(element[0], element[1], element[2])

        line = collinear(point_1_validated[0], point_1_validated[1],
                         point_2_validated[0], point_2_validated[1],
                         point_3_validated[0], point_3_validated[1])

        if line:
            result.add(line)

    return list(result)


def get_intersecting_lines_formatted(points):
    result = get_lines_intersect_three_or_more_points(points)
    return list([format_line(t) for t in result])

# Todo: make sure that there are no duplicates.
# Todo: make sure that the lists is greater than 2.
# Todo: make sure that


print(get_intersecting_lines_formatted([[1, 2], [1, 3], [1, 4]]))  # one line

print(get_intersecting_lines_formatted([[1, 2], [1, 3], [1, 4], [1, 7],
                                        [2, 3], [5, 9], [0, -1]]))  # 2 line
from pprint import pprint
pprint(get_intersecting_lines_formatted([[1, 2], [1, 3], [1, 4], [1, 7],
                                        [2, 3], [5, 9], [0, -1], [0.5, 0],
                                        [1, 1], [10, 10], [-4, -4]
                                         ]))  # 3 lines.


pprint(get_intersecting_lines_formatted([[1, 2], [1, 3], [1, 4], [1, 7],
                                        [2, 3], [5, 9], [0, -1], [0.5, 0],
                                        [1, 1], [3, 3], [-4, -4]
                                         ])) # 4 lines