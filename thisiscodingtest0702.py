def binary_search(array, target, start, end):
  if start > end:
    return 'no'

  mid = (start + end) // 2

  if array[mid] == target:
    return 'yes'
  elif array[mid] > target:
    return binary_search(array, target, start, mid-1)
  else:
    return binary_search(array, target, mid+1, end)
  
n = int(input())
stock = list(map(int,input().split()))
stock.sort()
m = int(input())
req = list(map(int,input().split()))

for i in req:
  print(binary_search(stock,i,0,len(stock)-1),end=' ')
