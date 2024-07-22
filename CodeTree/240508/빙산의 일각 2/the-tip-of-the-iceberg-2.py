#빙산의 개수
n = int(input())
heights = []
for _ in range(n):
    h = int(input())
    heights.append(h)

#빙산이 바다보다 높으면 True
def over(height, sea):
    return height > sea

ans = 0
#해수면 높이 최댓값은 1000
for i in range(1, 1001):
    #모든 빙산이 해수면에 잠기면 종료
    if max(heights) < i:
        break
    sea_level = i
    cnt = 0
    #첫 빙산이 해수면보다 높은지
    is_over = over(heights[0], sea_level)
    for j in range(n):  
        if is_over:
            #빙산 한 덩어리가 끝나는 지점
            if over(heights[j], sea_level) == False:
                is_over = False
                cnt += 1
                
        else:
            #빙산 한 덩어리가 시작하는 지점
            if over(heights[j], sea_level) == True:
                is_over = True
            
    #n번째 빙산이 마지막 빙산 덩어리에 포함되어 있는 경우
    if is_over:
        cnt += 1
    
    ans = max(ans, cnt)

print(ans)