import sys
#입력
n = int(input())
points = []
for _ in range(n):
    point = list(map(int, input().split()))
    points.append(point)

max_area = -sys.maxsize

#가우스 면적공식*2
def triangle(x1, y1, x2, y2, x3, y3):
    return abs((x1*y2 + x2*y3 + x3*y1) - (x2*y1 + x3*y2 + x1*y3))

def is_parellel(x1, y1, x2, y2):
    return x2-x1 == 0 or y2-y1 == 0

def cnt_parellel(x1, y1, x2, y2, x3, y3):
    cnt = 0
    if is_parellel(x1, y1, x2, y2):
        cnt += 1 
    if is_parellel(x1, y1, x3, y3):
        cnt += 1
    if is_parellel(x2, y2, x3, y3):
        cnt += 1
    return cnt

def is_same(x1, y1, x2, y2):
    return x1==x2 and y1==y2
#가능한 모든 세 점의 선택
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            x1, y1, x2, y2, x3, y3 = points[i][0], points[i][1], points[j][0], points[j][1], points[k][0], points[k][1]
            #동일한 점이 선택될 경우 삼각형 성립 불가
            if is_same(x1, y1, x2, y2) or is_same(x1, y1, x3, y3) or is_same(x2, y2, x3, y3):
                continue
            #한 변은 x축에 평행하며 다른 한 변은 y축에 평행
            if cnt_parellel(x1, y1, x2, y2, x3, y3) == 2:
                max_area = max(max_area, triangle(x1, y1, x2, y2, x3, y3))
                    
                
if max_area < 0:
    print(0)
else:
    print(max_area)