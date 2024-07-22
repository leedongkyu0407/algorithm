n = int(input())
first_c = list(map(int, input().split()))
second_c = list(map(int, input().split()))
#자물쇠
n_circle = [i for i in range(1, n+1)]

#조합 하나에 대하여 총 가능한 범위 계산 함수
def set_comb(c, n, n_circle):
    possible_comb = [[],[],[]]
    for i in range(3):
        for j in range(-2, 3):
            num = c[i]
            if num+j == -1:
                tmp = n_circle[-2]
            elif num+j == 0:
                tmp = n_circle[-1]
            
            elif num+j == n+1:
                tmp = n_circle[0]
            
            elif num+j == n+2:
                tmp = n_circle[1]
            #4
            #123
            #234
            else: 
                idx = num+j-1
                tmp = n_circle[idx]

            if tmp not in possible_comb[i]:
                possible_comb[i].append(tmp)
    
    return possible_comb

#가능한 비밀번호 조합 수
def full_count(c):
    sum_c = 1
    for i in range(len(c)):
        len_c = len(c[i])
        sum_c *= len_c
    
    return sum_c


ans = 0
if n == 1:
    ans = 1
elif n==2:
    ans = 8
else:
    first_comb = set_comb(first_c, n, n_circle)
    second_comb = set_comb(second_c, n, n_circle)

    #중복을 계산하지 않은 모든 비밀번호 조합의 수
    first_full_count = full_count(first_comb)
    second_full_count = full_count(second_comb)
    full_count = first_full_count+second_full_count
    #중복 제거
    for i in range(len(first_comb[0])):
        for j in range(len(first_comb[1])):
            for k in range(len(first_comb[2])):
                if first_comb[0][i] in second_comb[0] and first_comb[1][j] in second_comb[1] and first_comb[2][k] in second_comb[2]:
                    full_count -= 1
    ans = full_count

print(ans)