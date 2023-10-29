print('입력하세요')
n,m,k = map(int,input().split())
arr = list(map(int,input().split()))

sum = 0
arr.sort(reverse=True)

for i in range(1,m+1):
  if i%k == 0:
    sum += arr[1]
    continue
  sum += arr[0]

print(sum)
