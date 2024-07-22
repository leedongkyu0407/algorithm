n, k = map(int, input().split())
MAX_INT = 401
maps = [0]*MAX_INT

for _ in range(n):
    candy, position = map(int, input().split())
    maps[position] += candy


max_candy = 0
max_idx = 0
#중심점
for i in range(k, MAX_INT-k):
    sum_candy = 0
    for j in range(i-k, i+k+1):
        if maps[j]:
            sum_candy += maps[j]
    if max_candy < sum_candy:
        max_candy = sum_candy
        
    
print(max_candy)