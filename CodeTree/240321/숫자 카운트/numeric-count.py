n = int(input())
predicts = []
for i in range(n):
    input_data = list(map(int, input().split()))
    predicts.append(input_data)

#가능한 모든 경우의 수 탐색
def possible_num(a, b, c, strike, ball, prev_list):
    possible_list = []
    str_cnt, ball_cnt = 0, 0
    for i in range(1, 10):
        for j in range(1, 10):
            for k in range(1, 10):
                #조건 1 : 서로 다른 숫자 세 개 
                if i != j and j != k and k != i:
                    if i == a:
                        str_cnt += 1
                    if j==b:
                        str_cnt += 1
                    if k==c:    
                        str_cnt += 1
                    
                    if j==a or j==c:
                        ball_cnt += 1
                    if i==b or i==c:
                        ball_cnt += 1
                    if k==a or k==b:
                        ball_cnt += 1

                    #횟수에 따라 가짓수를 줄여가기 위해 prev_list 사용
                    if str_cnt == strike and ball_cnt == ball:
                        if len(prev_list) == 0 or [i, j, k] in prev_list:
                            possible_list.append([i,j,k])
                str_cnt, ball_cnt = 0, 0
    return possible_list
    
prev_list = []
for i in range(n):
    num, strike, ball = predicts[i]
    n1 = num//100
    n2 = (num-n1*100)//10
    n3 = (num-n1*100-n2*10)

    possible_list = possible_num(n1, n2, n3, strike, ball, prev_list)
    prev_list = possible_list
print(len(possible_list))