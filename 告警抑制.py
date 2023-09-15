# https://fcqian.blog.csdn.net/article/details/130768150
# 华为OD机试 - 告警抑制（Java & JS & Python）
#input
# 2
# A B
# B C
# A B C D E
#OUTPUT
# A D E
n=int(input())
yz=[]
for i in range(n):
    id1,id2= map(str,input().split())
    yz.append([id1,id2])
lb=input().split()
print(yz)
print(lb)
yzlb=[]
ha=dict()
yzha=dict()
for i in range(len(lb)):
    if lb[i] not in ha:
        ha[lb[i]]=lb[i]


for j in range(len(yz)):
    if yz[j][0] in ha:
        yzlb.append(yz[j][1])
        yzha[yz[j][1]]=yz[j][1]
out=[]
for i in range(len(lb)):
    if lb[i] not in yzha:
        out.append(lb[i])
out_string=" ".join(out)
print(out_string)