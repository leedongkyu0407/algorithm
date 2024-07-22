abilities = list(map(int, input().split()))
sum_a = sum(abilities)
t1, t2, t3 = 0, 0, 0
ans = 6000001
for i in range(6):
    for j in range(6):
        for k in range(6):
            for l in range(6):
                if i==j or i == k or i == l or j ==k or j==l or k==l:
                    continue
                
                t1 = abilities[i]+abilities[j]
                t2 = abilities[k]+abilities[l]
                t3 = sum_a - t1 - t2

                max_t = max(t1, t2, t3)
                min_t = min(t1, t2, t3)

                if max_t - min_t < ans:
                    ans = max_t - min_t
print(ans)