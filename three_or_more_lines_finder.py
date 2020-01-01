"""
## Author: Mohammad Mahjoub
## Copyright: Copyright 2020, lines_intersection
## License: Open Source
## Version: 1.0
## Maintainer: Mohammad Mahjoub
## Email: mmahjoub@westmont.edu
## Status: production
"""
from utilities import validate, collinear
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
        point_1_validated = validate(element[0])
        point_2_validated = validate(element[1])
        point_3_validated = validate(element[2])
        line, line2, line3 = collinear(point_1_validated[0], point_1_validated[1],
                                       point_2_validated[0], point_2_validated[1],
                                       point_3_validated[0], point_3_validated[1])

        if line and line not in result:
            result.append(line)

        if line2 and line2 not in result:
            result.append(line2)

        if line3 and line3 not in result:
            result.append(line3)

    return result


