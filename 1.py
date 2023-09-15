def generate_base_ids(start_id, end_id):
    # 解析左上角和右下角基地的编号，例如"A1" -> ("A", 1)
    start_letter, start_number = start_id[0], int(start_id[1])
    end_letter, end_number = end_id[0], int(end_id[1])

    base_ids = []

    for letter in range(ord(start_letter), ord(end_letter) + 1):
        for number in range(start_number, end_number + 1):
            base_ids.append(f"{chr(letter)}{number}")

    return base_ids

# 用户输入左上角和右下角的基地编号，用空格隔开
input_str = input("请输入左上角和右下角的基地编号，用空格隔开（例如，A1 F6）: ")
start_base, end_base = input_str.split()

# 生成基地编号数组
base_ids = generate_base_ids(start_base, end_base)

# 输出结果
print("选择的基地编号为:")
print(base_ids)