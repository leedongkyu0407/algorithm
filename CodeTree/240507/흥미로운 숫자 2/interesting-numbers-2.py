x, y = map(int, input().split())

def to_string_list(n):
    n = list(str(n))
    return n

#어떤 숫자들 몇 개로 이루어져 있는지 확인 함수
def cnt_num(a):
    dict_nums = {}
    for i in range(len(a)):
        if a[i] not in dict_nums:
            dict_nums[a[i]] = 1
        else:
            dict_nums[a[i]] += 1
    return dict_nums

#흥미로운 숫자인지 판별 함수
def is_interesting(dict_nums):
    #서로 다른 두 개의 숫자로만 구성
    if len(dict_nums) == 2:
        list_values = list(dict_nums.values())
        cnt = 0
        for n in list_values:
            #두 숫자 중 한 숫자가 한 자리만 차지
            if n == 1:
                return True

    return False

ans = 0
for i in range(x, y+1):
    num = to_string_list(i)
    dict_nums = cnt_num(num)
    if is_interesting(dict_nums):
        ans += 1

print(ans)