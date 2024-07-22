n = int(input())
n_list = list(map(int, input().split()))

#[1, 1], [2, 2]...[n, n]과 같이 구간 안에 원소가 하나일 경우 조건 만족
ans = 0
#시작점
for i in range(n):
    #끝점
    for j in range(i, n):
        s = 0
        avg = 0
        #구간 시작점과 끝점
        for k in range(i, j+1):
            s += n_list[k]
        avg = s/(j+1-i)
        if avg in n_list[i:j+1]:
            
            ans += 1
        

print(ans)