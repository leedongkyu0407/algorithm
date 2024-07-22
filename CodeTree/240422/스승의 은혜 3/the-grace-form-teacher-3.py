#학생 수(n) / 예산(b)
n, b = map(int, input().split())
#선물 가격(p) / 배송비(s)
prices_ship = []

for _ in range(n):
    p, s = map(int, input().split())
    prices_ship.append((p,s))

prices_ship.sort(key=lambda x:(x[0]+x[1], x[0]))

#선물 가능한 학생의 최대 명수
ans = 0
for i in range(n):
    #절반 가격으로 할 선물 선택
    half = prices_ship[i][0]//2
    pay = 0
    cnt = 0
    for j in range(n):
        if i == j:
            pay += half+prices_ship[j][1]
        else:
            pay += prices_ship[j][0]+prices_ship[j][1]
        cnt += 1
        
        if pay > b:
            ans = max(cnt-1, ans)
            break
print(ans)