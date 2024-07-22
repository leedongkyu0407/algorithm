import sys
#입력
n = int(input())
points = []
for _ in range(n):
    point = list(map(int, input().split()))
    points.append(point)

#거리의 제곱값 함수
def distance(x1, x2, y1, y2):
    return (x1-x2)**2 + (y1-y2)**2

min_dist = sys.maxsize

#모든 점들에 대하여 거리를 구하며 최소거리 찾기
for i, (x1, y1) in enumerate(points):    
    for j, (x2, y2) in enumerate(points):
        #동일한 두 점이 선택될 경우 다음 점으로 넘어감
        if j == i:
            continue
        min_dist = min(min_dist, distance(x1, x2, y1, y2))

print(min_dist)