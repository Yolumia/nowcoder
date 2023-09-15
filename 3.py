n, m = map(int, input().split())
a = list(map(int, input().split()))

anger = [0] * n  # 初始时每个人的愤怒值都是0
current_version = 0

for i in range(m):
    l, r = map(int, input().split())
    for j in range(l - 1, r):
        anger[j] += 1
    current_version += 1

    for j in range(n):
        if anger[j] > a[j]:
            print(current_version - 1)
            exit()

print(current_version)
