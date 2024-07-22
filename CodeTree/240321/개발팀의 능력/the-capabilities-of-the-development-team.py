abilities = list(map(int, input().split()))
sum_a = sum(abilities)
ans = 6001
flag = False
t1, t2, t3 = 0, 0, 0
for i in range(5):
    for j in range(5):
        for k in range(5):
            for l in range(5):
                if i==j or i==k or i==l or j==k or j==l or k==l:
                    continue
                
                t1 = abilities[i]+abilities[j]
                t2 = abilities[k]+abilities[l]
                t3 = sum_a - t1 - t2

                if t1 != t2 and t1 != t3 and t2 != t3:
                    max_t = max(t1, t2, t3)
                    min_t = min(t1, t2, t3)
                
                    if max_t-min_t < ans:
                        ans = max_t-min_t
                        flag = True

if flag:
    print(ans)
else:
    print(-1)