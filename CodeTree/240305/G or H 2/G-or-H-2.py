n = int(input())
MAX_INT = 101
maps = [0]*MAX_INT
positions = []

for _ in range(n):
    position, alpha = input().split()
    pos = int(position)
    if alpha == 'G':
        maps[pos] = 1
    else:
        maps[pos] = -1
    positions.append(pos)

#양쪽 끝 사이의 거리 함수
def sol(f, l):
    sum_alpha = 0
    flag = True
    length = 0
    for i in range(f, l+1):
        if maps[i] != maps[f]:
            flag = False
        sum_alpha += maps[i]
    
    if flag == True or sum_alpha == 0:
        length = l-f
        
    return length


positions.sort()
max_length = 0
#시작점
for i in range(n):
    #끝점
    for j in range(i+1, n):
        f, l = positions[i], positions[j]
        temp_len = sol(f, l)
        
        max_length = max(max_length, temp_len)

print(max_length)