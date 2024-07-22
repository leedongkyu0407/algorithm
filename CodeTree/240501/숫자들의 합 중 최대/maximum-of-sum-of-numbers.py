x, y = map(int, input().split())

ans = 0
for num in range(x, y+1):
    str_number = str(num)
    char_num = list(str_number)
    int_list = list(map(int, char_num))
    digit_sum = sum(int_list)

    ans = max(ans, digit_sum)

print(ans)