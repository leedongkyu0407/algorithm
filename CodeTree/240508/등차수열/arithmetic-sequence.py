n = int(input())
n_list = list(map(int, input().split()))


#k의 최댓값은 100
max_k = 0
#삽입할 수 k
for k in range(1, 101):
    #두 수를 선택
    cnt = 0
    for i in range(n):
        for j in range(i+1, n):
            #등차수열 공식
            #a, b, c로 이루어진 수열이 등차수열이라면 (a+c)/2 = b
            if (n_list[i]+n_list[j])/2 == k:
                cnt += 1
    
    max_k = max(max_k, cnt)

print(max_k)