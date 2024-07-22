n = int(input())
points = []
for _ in range(n):
    a, b = map(int, input().split())
    points.append((a, b))

ans = 0
#제외할 세 개의 선분 선택
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            #선분 point를 리스트로 표현
            lines = [0]*101
            flag = True
            #전체 범위 완전탐색
            for l in range(n):
                #제외할 선분일 경우 
                if l == i or l==j or l==k:
                    continue
                for m in range(points[l][0], points[l][1]+1):
                    lines[m] += 1
                    if lines[m]>1:
                        flag = False
                
            if flag:
                ans += 1

print(ans)