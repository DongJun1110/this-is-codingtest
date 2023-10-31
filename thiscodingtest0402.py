di = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}
steps = [(-2,-1),(-1,-2),(1,-2),(-2,1),(2,1),(1,2),(-1,2),(2,-1)]

location = input()

row = int(location[1])
col = int(di.get(location[0]))
result = 0

for step in steps:
    x = col + step[0] 
    y = row + step[1]
    if 0<x<9 and 0<y<9:
        result += 1

print(result)
