#사람 수 / 치즈 수 / 치즈를 먹은 기록의 수 / 아픈 기록의 수
n, m, d, s = map(int, input().split())

#몇번째 사람(p)이 몇 번째 치즈(m)를 언제 먹었는지(t)
eatings = []
for _ in range(d):
    p, m, t = map(int, input().split())
    eatings.append((p, m, t))

#몇 번 째 사람(p)이 언제 확실히 아팠는지(t)
#상한 치즈를 먹은 1초 뒤에 아프기 시작
sick = []
for _ in range(s):
    p, t = map(int, input().split())
    sick.append((p, t))

#사람(p) / 시간(t)에 따라 정렬
eatings.sort(key=lambda x:(x[0], x[2]))

#중복제거를 위해 집합 자료형 사용
medicine = set()
#상한 가능성이 있는 치즈들
candidate = []

#확실히 아픈 사람들을 이용해서 상할 가능성이 있는 치즈 찾기
for i in range(s):
    #아픈 사람(sick_p), 아픈 시간(sick_t)
    sick_p, sick_t = sick[i]

    for j in range(d):
        #몇번째 사람(eat_p)이 몇 번째 치즈(eat_m)를 언제 먹었는지(eat_t)
        eat_p, eat_m, eat_t = eatings[j]
        #확실히 아픈 시간 이전에도 아팠을 가능성이 존재
        if (sick_p == eat_p) and (eat_t < sick_t):
            candidate.append(eat_m)
            medicine.add(eat_p)

#위의 정보를 바탕으로 상한 것일 확률이 있는 치즈를 먹은 다른 사람 찾기
for k in range(d):
    eat_p, eat_m, eat_t = eatings[k]
    if eat_m in candidate:
        medicine.add(eat_p)

print(medicine)
print(len(medicine))