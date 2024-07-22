#폭탕늬 개수(n) / 특정 거리(k)
n, k = map(int, input().split())

bombs = []
for _ in range(n):
    b = int(input())
    bombs.append(b)

ans = 0
for i in range(n):
    for j in range(i+1, n):
        #폭탄 번호가 동일하고 둘 사이의 거리가 k이내일 때
        if (bombs[i] == bombs[j]) and (j-i) <= k:
            ans = max(ans, bombs[i])

if ans == 0:
    print(-1)
else:
    print(ans)