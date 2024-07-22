n = int(input())
maps = []
max_idx = []

for _ in range(n):
    l = list(map(int, input().split()))
    maps.append(l)

def in_range(x, y):
    return x>=0 and x<n and y>=0 and y<n

#1*3씩 격자 탐색 함수
def sol(n):
    ans = 0
    for i in range(n):
        for j in range(n-2):
            cnt = 0
            start_x, start_y = i, j
            for k in range(3):
                nx, ny = start_x, start_y+k
                if in_range(nx, ny) and maps[nx][ny]==1:
                    cnt +=1
            
            if ans<cnt:
                max_idx.append([start_x, start_y])    
                ans = cnt                

    return ans

#1차 탐색 후 최댓값
first_box = sol(n)
#1차 탐색 결과값 격자에서 제외해주기
if max_idx:
    rx, ry = max_idx[-1][0], max_idx[-1][1]
    for i in range(3):
        nx, ny = rx, ry+i
        maps[nx][ny] = 0
#2차 탐색 후 최댓값
second_box = sol(n)
print(first_box+second_box)