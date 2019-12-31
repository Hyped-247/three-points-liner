"""
    You can take two points, find a passing line
    and check if any other given Done.
    point passes through same line (for this u can substitute x and y values with point
    and then check if equation is true on LHS and RHS)
"""


def lines_intersection(list_points):
    """
    :param list_points:
    :return:
    :raise TypeError
    """
    if len(list_points) <= 2:
        return []

    list_points_len = len(list_points)
    result = list()

    p1 = 0
    p2 = 1
    p3 = 2

    while True:
        while p3 != list_points_len and p2 != list_points_len:
            if p3 == p1 or p3 == p2:
                p3 += 1
            else:
                result.append([mo[p1], mo[p2], "=====>", mo[p3]])
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



    # while found_next:
    #     if list_points_len - 2 != counter:
    #         p1 = validate(list_points[counter])
    #         p2 = validate(list_points[counter + 1])
    #         p3 = validate(list_points[counter + 2])
    #         a, b, c = find_line_given_two_points(p1, p2)
    #         if is_on_line(a, b, c, p3):
    #             line = {'a': a, 'b': b, 'c': c}
    #             result.append(line)
    #         counter += 1
    #     else:
    #         found_next = False
    # return result


def validate(point):
    if isinstance(point, list):
        if len(point) == 2:
            first_element = point[0]
            second_element = point[1]
            if not isinstance(first_element, int) and not isinstance(second_element, int):
                raise TypeError("The points list must only contain numbers.")
            return point
        else:
            raise Exception("Each list of points must contain two integers.")
    else:
        raise TypeError("Please input a list of points.")


def find_line_given_two_points(p, q):
    """
    :param p:
    :param q:
    :return: line values.
    """
    a = q[1] - p[1]
    b = p[0] - q[0]
    c = formula(a, b, p)
    return a, b, c


def formula(a, b, point):
    return (a * (point[0])) + (b * (point[1]))


def is_on_line(a, b, c, point):
    return formula(a, b, point) * (point[1]) == c


if __name__ == '__main__':
    list_points = [[1, 2], [1, 1], [2, 3]]
    find_line_given_two_points(list_points[0], list_points[1])
    find_line_given_two_points(list_points[0], list_points[2])
    find_line_given_two_points(list_points[1], list_points[2])
    # print(is_on_line(-1, 0, -1, [1, 3]))
    #  lines_intersection(list_points)




