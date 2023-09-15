# 输入A村和B村各农户农业产值数据
a_village_data = input()
b_village_data = input()

# 将输入的数据字符串分割为列表，并合并成一个列表
a_data_list = [float(x) for x in a_village_data.split(',')]
b_data_list = [float(x) for x in b_village_data.split(',')]
merged_data = sorted(a_data_list + b_data_list)

# 计算中位数
total_count = len(merged_data)
if total_count % 2 == 1:
    median = merged_data[total_count // 2]
else:
    mid1 = merged_data[total_count // 2 - 1]
    mid2 = merged_data[total_count // 2]
    median = (mid1 + mid2) / 2

# 输出中位数
print(median)
