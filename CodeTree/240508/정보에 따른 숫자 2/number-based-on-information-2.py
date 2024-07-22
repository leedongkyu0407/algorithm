#알파벳 개수 / x시작점 / x 끝점
T, a, b = map(int, input().split())
S_pos = []
N_pos = []
for _ in range(T):
    alpha, pos = input().split()
    if alpha == 'S':
        S_pos.append(int(pos))
    else:
        N_pos.append(int(pos))

S_pos.sort()
N_pos.sort()

#알파벳 S까지의 거리 d1이 알파벳 N까지의 거리 d2보다 작거나 같은 경우
def is_special(d1, d2):
    return d1 <= d2

#가장 가까운 점 찾는 함수
def min_d(pos_list, k):
    #알파벳이 놓이는 최대 거리 차이는 1,000 미만
    minimum = 1001
    for p in pos_list:
        minimum = min(minimum, abs(p-k))
    return minimum

ans = 0
#현재 점 k
for k in range(a, b+1):
    d1 = min_d(S_pos, k)
    d2 = min_d(N_pos, k)
    if is_special(d1, d2):
        ans += 1

print(ans)