n = int(input())
max_R = 1000000
points = []
for _ in range(n):
    x1, x2 = map(int, input().split())
    points.append((x1+max_R, x2+max_R))

ans = 0
for i in range(n):
    overlap = False
    #기준선분
    x1, x2 = points[i]
    for j in range(n):
        #자기 자신 제외
        if i == j:
            continue
        
        #비교선분
        x3, x4 = points[j]
        
        #x1이 큰 쪽이 x2가 더 작으면 선분은 겹침
        if (x1>x3 and x2<x4) or (x1<x3 and x2>x4):
            overlap = True
            break
            
    if overlap == False:
        ans += 1

print(ans)