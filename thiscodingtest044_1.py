n = int(input())
first, second = 0,0
command = list(input().split())
for j in command:

    if j == 'R':
        if second == n-1:
            continue
        second += 1
    elif j == 'L':
        if second == 0:
            continue
        second -= 1
    elif j == 'U':
        if first == 0:
            continue
        first -= 1
    elif j == 'D':
        if first == n-1:
            continue
        first +=1 
    

print(first+1, second+1)
        