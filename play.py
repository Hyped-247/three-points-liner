
mo = [1, 2, 3, 4]
result = list()
len_list = len(mo)
p1 = 0
p2 = 1
p3 = 2
# p1=0, p2=1, p3=0
# [1, 2, 3]
#  ^     ^
#     ^

while True:
    while p3 != len_list and p2 != len_list:
        if p3 == p1 or p3 == p2:
            p3 += 1
        else:
            result.append([mo[p1], mo[p2], "=====>", mo[p3]])
            p3 += 1

    if p1 == len_list - 2 and p2 == len_list:
        break

    if p3 == len_list:
        p3 = 0
        p2 += 1
    else:
        p3 = 0
        p1 += 1
        p2 = p1 + 1

for i in result:
    print(i)