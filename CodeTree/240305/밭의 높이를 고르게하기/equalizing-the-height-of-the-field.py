import sys
n, h, t = map(int, input().split())
maps = list(map(int, input().split()))

min_cost = sys.maxsize 
#시작점
for i in range(n-t+1):
    cost = 0
    #끝점(T번 나오도록)
    for j in range(i, i+t):
        now_h = maps[j]
        cost = cost + abs(now_h - h)
    
    min_cost = min(cost, min_cost)

print(min_cost)