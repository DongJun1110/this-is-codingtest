n = int(input())
first, second = 0,0
command = list(input().split())
for j in command:

    if j == 'R':
        if second != n-1:
            second += 1
    elif j == 'L':
        if second != 0:
            second -= 1
    elif j == 'U':
        if first != 0:
            first -= 1
    elif j == 'D':
        if first != n-1:
            first +=1 

print(first+1, second+1)
        