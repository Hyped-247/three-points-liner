"""
## Author: Mohammad Mahjoub
## Copyright: Copyright 2020, three_or_more_lines_finder
## License: Open Source
## Version: 1.0
## Maintainer: Mohammad Mahjoub
## Email: mmahjoub@westmont.edu
## Status: maintenance
"""
from utilities import collinear, add_lines, validate_points
from itertools import combinations


def three_or_more_lines_finder(list_points):
    """
    :param list_points: a list containing lists of points.
    :return: a list of lines.
    :raise TypeError
    """
    list_points_len = len(list_points)
    if list_points_len <= 2:
        return []

    result = list()
    perm = list(combinations(list_points, 3))

    for element in perm:
        point_1_validated, point_2_validated, point_3_validated = \
            validate_points(element[0], element[1], element[2])

        line, line2, line3 = collinear(point_1_validated[0], point_1_validated[1],
                                       point_2_validated[0], point_2_validated[1],
                                       point_3_validated[0], point_3_validated[1])

        add_lines(line, line2, line3, result)

    return result

