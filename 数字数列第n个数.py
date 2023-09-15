n = int(input())
s=""
for i in range(0,3000,2):
   s=s+i.__str__()
print(s[n-1])
