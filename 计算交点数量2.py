def find_intersection(line1, line2):
    x1, y1 = line1[0]
    x2, y2 = line1[1]
    x3, y3 = line2[0]
    x4, y4 = line2[1]


    if (x1 == x2 and x3 == x4) or (y1 == y2 and y3 == y4):
        return None  # 平行线或共线，没有交点


    if  (y1-y2)/(x1-x2) == (y3-y4)/(x3-x4):
        return None
    # if (k1-k2)<=10^(-4):
    #     return None

    # 计算直线1和直线2的交点坐标
    e = 10 ^ (-10)
    x = (y4 - y3 + (x3 * (y1 - y2) - x1 * (y3 - y4)) / (x1 - x2)) / (((y1 - y2) / (x1 - x2) - (y3 - y4) / (x3 - x4))  )

    y = (x - x1) * (y1 - y2) / (x1 - x2) + y1

    # if abs(x) > 65536:
    #     return None
    # if abs(y) > 65536:
    #     return None
    x = int(x * 100)
    y = int(y * 100)

    return (x, y)


def count_intersections(lines):
    intersections = set()
    n = len(lines)

    for i in range(n):
        for j in range(i + 1, n):
            intersection = find_intersection(lines[i], lines[j])
            if intersection:
                intersections.add(intersection)

    return len(intersections)


# 输入示例
lines = [((1, 1), (2, 2)), ((3, 3), (4, 4)), ((1, 2), (2, 1)), ((1, 1), (4, 4))]
intersection_count = count_intersections(lines)
print("交点数量:", intersection_count)
