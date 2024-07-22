#장비 개수/Ta보다 낮을 때 작업량/Ta 이상 Tb이하일 때 작업량/Tb 이상일 때 작업량
n, c, g, h = map(int, input().split())
tas = []
tbs = []
for _ in range(n):
    ta, tb = map(int, input().split())
    tas.append(ta)
    tbs.append(tb)

min_t = min(tas)
max_t = max(tas)

max_amount = 0
for t in range(min_t, max_t+1):
    temp_amount = 0
    for i in range(n):
        if t < tas[i]:
            amount = c
        elif t >= tas[i] and t <= tbs[i]:
            amount = g
        elif t > tbs[i]:
            amount = h
        
        temp_amount += amount
    
    max_amount = max(max_amount, temp_amount)

print(max_amount)