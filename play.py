from utilities import find_line_given_two_points

# Get all permutations of [1, 2, 3]
# perm = combinations([1, 2, 3, 4], 3)
#
# print(list(takewhile(lambda x: len(x) <= 2, [(1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4)])))
# print(list(perm))
# # Print the obtained permutations
# for i in perm:
#     print(i)


def collinear(x1, y1, x2, y2, x3, y3):
    if (y3 - y2) * (x2 - x1) == (y2 - y1) * (x3 - x2):
        print("Yes")
        print("(y3 - y2)", (y3 - y2))
        print("(x2 - x1)", (x2 - x1))
        print("(y2 - y1)", (y2 - y1))
        print("(x3 - x2)", (x3 - x2))
        print(find_line_given_two_points([x3, y1], [y2, y3]))
        print(find_line_given_two_points([x1, x2], [x3, y1]))
    else:
        print("No")


x1, x2, x3, y1, y2, y3 = 1, 1, 1, 1, 4, 5

collinear(x1, y1, x2, y2, x3, y3)

