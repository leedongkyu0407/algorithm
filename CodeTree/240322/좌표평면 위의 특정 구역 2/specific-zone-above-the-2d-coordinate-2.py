import sys
n = int(input())
points = []
for _ in range(n):
    point = list(map(int, input().split()))
    points.append(point)

min_area = sys.maxsize

for i in range(n):
    max_x, max_y, min_x, min_y = 0, 0, 40001, 40001
    for j in range(n):
        if i == j:
            continue
        
        x, y = points[j][0], points[j][1]
        if x > max_x:
            max_x = x
        if x < min_x:
            min_x = x
        if y > max_y:
            max_y = y
        if y < min_y:
            min_y = y
        
    area = (max_x-min_x)*(max_y-min_y)
    min_area = min(min_area, area)

print(min_area)