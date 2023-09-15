# 输入汇报总数和需要关注的部落数量
p, q = map(int, input().split())

# 输入所有汇报所属的部落编号
report_belongs_to_tribe = list(map(int, input().split()))

# 输入需要关注的部落编号，并建立一个字典来记录关注部落的顺序
focus_tribes = list(map(int, input().split()))
focus_tribe_order = {}
for i in range(q):
    focus_tribe_order[focus_tribes[i]] = i

# 构建一个列表，用于存储所有汇报信息以及对应的部落编号和关注部落顺序
reports = []
for i in range(p):
    reports.append((report_belongs_to_tribe[i], i))

# 对汇报进行排序，首先按照是否为关注部落分组，然后按照关注部落的顺序和部落编号排序
reports.sort(key=lambda x: (focus_tribe_order.get(x[0], q), x[0]))

# 输出排序后的汇报所属部落的编号
for report in reports:
    print(report[0], end=" ")
