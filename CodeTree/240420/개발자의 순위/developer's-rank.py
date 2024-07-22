#k 번의 경기 n명의 개발자
k,n = map(int, input().split())
rank = []
for _ in range(k):
    input_r = list(map(int, input().split()))
    rank.append(input_r)

ans = 0
for i in range(1, n+1):
    for j in range(i+1, n+1):
        cnt = 0
        for m in range(k):
            #각 개발자별 인덱스 비교
            if rank[m].index(i) < rank[m].index(j):
                cnt += 1
            elif rank[m].index(i) > rank[m].index(j):
                cnt -= 1
        #순위가 불변하다면 abs(cnt)의 값이 경기 수 k와 동일
        if abs(cnt) == k:
            ans += 1

print(ans)