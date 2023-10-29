n,m = map(int,input().split())
min_value = []
for i in range(n):
  li = list(map(int,input().split()))
  min_value.append(min(li))

min_value.sort()
print(min_value[n-1])
