# 输入字符串
input_str = input()

# 初始化一个空字符串用于存储结果
result_str = ''

# 遍历输入字符串，将非重复字符添加到结果字符串中
for char in input_str:
    if  result_str.count(char) ==0:
        result_str += char

# 对结果字符串进行降序排序
unique_sorted_str = ''.join(sorted(result_str, reverse=True))

# 输出结果
print(unique_sorted_str)