def find_intersection(line1, line2):
    x1, y1 = line1[0]
    x2, y2 = line1[1]
    x3, y3 = line2[0]
    x4, y4 = line2[1]

    if (x1 == x2 and x3 == x4) or (y1 == y2 and y3 == y4):
        return None  # 平行线或共线，没有交点

    # 计算直线1和直线2的交点坐标
    x = (y4 - y3 + (x3 * (y1 - y2) - x1 * (y3 - y4)) / (x1 - x2)) / ((y1 - y2) / (x1 - x2) - (y3 - y4) / (x3 - x4))
    y = (x - x1) * (y1 - y2) / (x1 - x2) + y1

    return (round(x, 2), round(y, 2))


def count_intersections(lines):
    intersections = set()
    n = len(lines)

    for i in range(n):
        for j in range(i + 1, n):
            intersection = find_intersection(lines[i], lines[j])
            if intersection:
                intersections.add(intersection)

    return len(intersections)


# 从键盘输入获取直线坐标
input_str = input()#"请输入直线坐标，使用格式{(x1,y1),(x2,y2)}|{(x3,y3),(x4,y4)}： "
input_lines = input_str.split("|")
lines = []

for line_str in input_lines:
    points = line_str.strip("{}").split(",")
    line = ((int(points[0][1:]), int(points[1][:-1])), (int(points[2][1:]), int(points[3][:-1])))
    lines.append(line)

intersection_count = count_intersections(lines)
print(intersection_count)#"交点数量:"
