def calculate_intersection_area(rect1, rect2):
    x1 = max(rect1[0], rect2[0])
    y1 = max(rect1[1], rect2[1])
    x2 = min(rect1[2], rect2[2])
    y2 = min(rect1[3], rect2[3])

    if x1 < x2 and y1 < y2:
        return (x2 - x1) * (y2 - y1)
    else:
        return 0
def calculate_union_area(rect1, rect2):
    area_rect1 = (rect1[2] - rect1[0]) * (rect1[3] - rect1[1])
    area_rect2 = (rect2[2] - rect2[0]) * (rect2[3] - rect2[1])
    intersection_area = calculate_intersection_area(rect1, rect2)
    union_area = area_rect1 + area_rect2 - intersection_area
    return union_area
def calculate_iou(rect1, rect2):
    intersection_area = calculate_intersection_area(rect1, rect2)
    union_area = calculate_union_area(rect1, rect2)
    iou = intersection_area / union_area
    return iou

if __name__ == "__main__":
    rect1 = list(map(int, input().split()))
    rect2 = list(map(int, input().split()))
    iou = calculate_iou(rect1, rect2)
    print(iou)
