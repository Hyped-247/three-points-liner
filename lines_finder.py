"""
## Author: Mohammad Mahjoub
## Copyright: Copyright 2020, get_lines_intersect_three_or_more_points
## License: Open Source
## Version: 1.0
## Email: mmahjoub@westmont.edu
## Status: maintenance
"""
from utilities import collinear, validate_points
from itertools import combinations


def collinear(x1, y1, x2, y2, x3, y3):
    """
    if....3 points are ...


    :param x1: number
    :param y1: number
    :param x2: number
    :param y2: number
    :param x3: number
    :param y3: number
    :return: tuple of dictionary lines or tuple of Nones
    """
    if (y3 - y2) * (x2 - x1) == (y2 - y1) * (x3 - x2):
        # they are colinear.
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


"""


  '-8x + 4y = -4' => -1* -8/4 , -4/4 => (2, -1)
  '-4x + 2y = -2' => -1* -4/2 , -2/1 => (2, -1)


          y = 2x - 1



   (1, 2), (1, 3), (1, 4), (1, 5) => x = 1 => 1x + 0y = 1
"""


def get_lines_intersect_three_or_more_points(list_points):
    """
    :param list_points: a list containing lists of points (ex. [[5, 9], [6, 8], [3, 5]])
    :return: a list of dictionaries (ex.[{'a': -8, 'b': 4, 'c': -4, 'formatted_line': '-8x + 4y = -4'}, ...]).
    :raise TypeError if list_points is not a list of lists.
    """
    list_points_len = len(list_points)
    # Todo: throw an error if points are the same.

    if list_points_len <= 2:
        return []

    result = set()
    perm = list(combinations(list_points, 3))

    for element in perm:
        point_1_validated, point_2_validated, point_3_validated = \
            validate_points(element[0], element[1], element[2])

        line, line2, line3 = collinear(point_1_validated[0], point_1_validated[1],
                                       point_2_validated[0], point_2_validated[1],
                                       point_3_validated[0], point_3_validated[1])


        result.add(line)
        add_lines(line, line2, line3, result)

    return result

