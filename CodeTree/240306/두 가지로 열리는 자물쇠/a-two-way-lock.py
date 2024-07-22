n = int(input())
first_c = list(map(int, input().split()))
second_c = list(map(int, input().split()))

#조합 하나에 대하여 총 가능한 범위 계산 함수
def set_range(c):
    comb_range = [[0]*5 for _ in range(3)]
    for i in range(3):
        for j in range(-2, 3):
            num = c[i]
            if num+j == 0:
                tmp = n
            elif num+j == -1:
                tmp = n-1
            
            elif num+j == n+1:
                tmp = 1
            
            elif num+j == n+2:
                tmp = 2
            
            else: tmp = num+j


            comb_range[i][j+2] = tmp

    return comb_range

first_range = set_range(first_c)
second_range = set_range(second_c)

#중복을 계산하지 않은 모든 비밀번호 조합의 수
full_count = 2*5*5*5
#중복 제거
for i in range(5):
    for j in range(5):
        for k in range(5):
            if first_range[0][i] in second_range[0] and first_range[1][j] in second_range[1] and first_range[2][k] in second_range[2]:
                full_count -= 1

print(full_count)