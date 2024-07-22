n, k = map(int, input().split())
MAX_INT = 10001
maps = [0]*MAX_INT

for _ in range(n):
    position, alpha = input().split()
    if alpha == 'G':
        maps[int(position)] = 1
    elif alpha == 'H':
        maps[int(position)] = 2

ans = 0 
for i in range(MAX_INT-k):
    cnt = 0
    for j in range(i, i+k+1):
        if maps[j]:
            cnt += maps[j]

    ans = max(ans, cnt)

print(ans)