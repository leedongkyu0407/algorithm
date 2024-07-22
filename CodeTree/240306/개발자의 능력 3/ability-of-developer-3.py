import sys
abilities = list(map(int, input().split()))

min_diff = sys.maxsize
for i in range(6):
    for j in range(i+1, 6):
        for k in range(j+1, 6):
            sum_a = abilities[i]+abilities[j]+abilities[k]
            sum_b = sum(abilities)-sum_a

            min_diff = min(min_diff, abs(sum_b-sum_a))

print(min_diff)