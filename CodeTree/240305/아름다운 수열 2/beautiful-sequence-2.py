n, m = map(int, input().split())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

ans = 0
#시작점

for i in range(n-m+1):
    temp_list = b_list[:]
    for j in range(m):
        if a_list[i+j] in temp_list:
            temp_list.remove(a_list[i+j])
        if not temp_list:
            ans += 1
           
print(ans)