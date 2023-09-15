def find_survivor(m, n):
    # 创建一个编号列表
    people = list(range(1, m + 1))
    index = 0

    while len(people) > 1:
        # 计算要删除的人的索引
        index = (index + n - 1 ) % len(people)
        # 移除被淘汰的人
        people.pop(index)

    return people[0]

# 从控制台输入m和n
input_str = input("请输入m和n（用空格分开）：")
m, n = map(int, input_str.split())

# 查找幸存者并输出
result = find_survivor(m, n)
print("幸存者的编号是:", result)
