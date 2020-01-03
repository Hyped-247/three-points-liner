from collections import Counter


def validate_three_points(p1: list, p2: list, p3: list) -> tuple:
    """
    Validate three given points.
    If all three points are valid, then it will return back.
    Otherwise, it will throw a ValueError.
    :param p1: list of two numbers
    :param p2: list of two numbers
    :param p3: list of two numbers
    :return: a tuple of three validated lists
    """
    return validate_list_point(p1), validate_list_point(p2), validate_list_point(p3)


def validate_list_point(point: list) -> list or TypeError:
    """
    Validates the input data. If the input data is a list
    containing two numbers, then the will return that list.
    Otherwise, it will throw a TypeError.
    :param point: a list containing two numbers
    :return: validated point list
    :raise TypeError if point is not a list that contains two numbers
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


def validate_has_duplicates(points: list) -> bool:
    """
    Checks if a list points contain any duplicates.
    :param points: a list containing non duplicates lists of points (ex. [[5, 9], [6, 8], [3, 5]])
    :return: bool
    """
    c = Counter(map(tuple, points))
    non_duplicate_list = [k for k, v in c.items() if v > 1]
    return len(non_duplicate_list) > 0
