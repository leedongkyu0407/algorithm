n = int(input())
workers = []
for _ in range(n):
    t = tuple(map(int, input().split()))
    workers.append(t)

max_time = 0
for i in range(n):
    times = [0]*1001
    for j in range(n):
        #해고할 index
        if i==j:
            continue
        
        s, e = workers[j]
        for k in range(s, e):
            times[k] = 1
        
        max_time = max(max_time, sum(times))

print(max_time)