import sys
n, k = map(int, input().split())
n_list = list(map(int, input().split()))

sum_max = -sys.maxsize

for i in range(n-k+1):
    s = 0
    for j in range(k):
        s += n_list[i+j]
    
    sum_max = max(sum_max, s)

print(sum_max)