#사람의 수 / 치즈의 수 / 치즈를 먹은 기록의 수 / 아픈 기록의 수 
n, m, d, s = map(int, input().split())
#몇번째 사람(p)이 몇 번째 치즈(m)를 언제 먹었는지(t)
eatings = []
for _ in range(d):
    eat_p, eat_m, eat_t = map(int, input().split())
    eatings.append((eat_p, eat_m, eat_t))

#몇 번째 사람(p)이 언제 확실히 아팠는지(t)
sick = []
for _ in range(s):
    sick_p, sick_t = map(int, input().split())
    sick.append((sick_p, sick_t))


#각 치즈별 완전탐색
rotten = []
for i in range(m):
    cheeze = i+1
    #아픈 사람 모두가 먹었는지 확인하기 위한 지표
    flag = 0
    for j in range(s):
        sick_p, sick_t = sick[j]
        for k in range(d):
            eat_p, eat_m, eat_t = eatings[k]
            if (eat_m == cheeze) and (sick_p == eat_p) and (sick_t > eat_t):
                flag += 1

    #아픈 사람 모두가 해당 치즈를 먹었을 경우 상했을 가능성이 있는 치즈
    if flag >= s:
        rotten.append(cheeze)

ans = 0
#상한 치즈를 먹은 사람들을 위한 약이 최대 몇 개나 필요한지
for l in range(len(rotten)):
    rot = rotten[l]
    #중복 제거를 위한 집합 자료형
    temp = set()
    for m in range(d):
        eat_p, eat_m, eat_t = eatings[m]
        if eat_m == rot:
            temp.add(eat_p)
    
    ans = max(ans, len(temp))

print(ans)