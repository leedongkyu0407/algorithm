n, B = map(int, input().split())
price = []
for _ in range(n):
    p = int(input())
    price.append(p)

#선물 가격 정렬
price.sort()
ans = 0

for i in range(n):
    #반값 선물
    pi = price[i]//2
    people = 0
    b = B

    #가장 많은 학생에게 선물을 줄 때의 학생 수
    
    for j in range(n):
        if i == j:
            p = pi
        else:
            p = price[j]
        
    #p = 선물 가격 / b = 현재 남은 돈    
        if b - p >= 0:
            b -= p
            people += 1
    
    ans = max(people, ans)

print(ans)