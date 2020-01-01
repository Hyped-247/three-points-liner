"""
## Author: Mohammad Mahjoub
## Copyright: Copyright 2020, lines_intersection
## License: Open Source
## Version: 1.0
## Maintainer: Mohammad Mahjoub
## Email: mmahjoub@westmont.edu
## Status: production
"""
from utilities import find_line_given_two_points, is_on_line, validate


def lines_intersection(list_points):
    """
    :param list_points: a list containing lists of points.
    :return: a list of lines.
    :raise TypeError
    """
    list_points_len = len(list_points)
    if list_points_len <= 2:
        return []

    result = list()
    p1, p2, p3 = 0, 1, 2

    while True:
        while p3 != list_points_len and p2 != list_points_len:
            if p3 == p1 or p3 == p2:
                p3 += 1
            else:
                point_1_validated = validate(list_points[p1])
                point_2_validated = validate(list_points[p2])
                point_3_validated = validate(list_points[p3])

                a, b, c = find_line_given_two_points(point_1_validated, point_2_validated)
                if is_on_line(a, b, c, point_3_validated):
                    line = {'a': a, 'b': b, 'c': c}
                    if line not in result:  # remove duplicates.
                        result.append(line)
                p3 += 1

        if p1 == list_points_len - 2 and p2 == list_points_len:
            break

        if p3 == list_points_len:
            p3 = 0
            p2 += 1
        else:
            p3 = 0
            p1 += 1
            p2 = p1 + 1

    return result


if __name__ == '__main__':
    list_points = [[5, 9], [6, 8], [3, 5]]
    print(lines_intersection(list_points))
    print(find_line_given_two_points(list_points[0], list_points[2]))




