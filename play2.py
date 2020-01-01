from utilities import find_line_given_two_points, validate, format_line
from itertools import combinations


_list = [[1, 1], [1, 4], [1, 5]]

perm = list(combinations(_list, 3))
print(perm)


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
    print(list_points)
    perm = list(combinations(list_points, 3))
    for element in perm:
        point_1_validated = validate(element[0])
        point_2_validated = validate(element[1])
        point_3_validated = validate(element[2])
        line, line2, line3 = collinear(point_1_validated[0], point_1_validated[1],
                                point_2_validated[0], point_2_validated[1],
                                point_3_validated[0], point_3_validated[1])

        if line not in result:
            result.append(line)

        if line2 not in result:
            result.append(line2)

        if line3 not in result:
            result.append(line3)

    return result


def collinear(x1, y1, x2, y2, x3, y3):
    if (y3 - y2) * (x2 - x1) == (y2 - y1) * (x3 - x2):
        a, b, c = find_line_given_two_points([x1, y1], [x2, y2])
        line = {'a': a, 'b': b, 'c': c, "formatted_line": format_line(a, b, c)}

        a, b, c = find_line_given_two_points([x2, y2], [x3, y3])
        line2 = {'a': a, 'b': b, 'c': c, "formatted_line": format_line(a, b, c)}

        a, b, c = find_line_given_two_points([x1, y1], [x3, y3])
        line3 = {'a': a, 'b': b, 'c': c, "formatted_line": format_line(a, b, c)}

        return line, line2, line3

    return None, None

# [{'a': -8, 'b': 4, 'c': -4, 'formatted_line': '-8x + 4y = -4'},
# {'a': 0, 'b': 0, 'c': 0, 'formatted_line': '0x + 0y = 0'},
# {'a': 2, 'b': -1, 'c': 1, 'formatted_line': '2x -1y = 1'}]

# [{'a': -8, 'b': 4, 'c': -4, 'formatted_line': '-8x + 4y = -4'},
# {'a': -6, 'b': 3, 'c': -3, 'formatted_line': '-6x + 3y = -3'},
# {'a': 0, 'b': 0, 'c': 0, 'formatted_line': '0x + 0y = 0'},
# {'a': 2, 'b': -1, 'c': 1, 'formatted_line': '2x -1y = 1'}]


print(three_or_more_lines_finder(_list))



