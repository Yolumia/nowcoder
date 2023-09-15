income_data = input("请输入家庭的收入数据（用空格分隔）：").split()
income_list = [int(income) for income in income_data]

# 初始化计数器
count = 0

# 遍历每一个家庭的收入
for i in range(len(income_list)):
    current_income = income_list[i]

    # 检查是否当前家庭的收入至少比一户家庭高，又至少比一户家庭低
    if current_income != max(income_list) and current_income != min(income_list):
        count += 1

# 输出结果
print(count)