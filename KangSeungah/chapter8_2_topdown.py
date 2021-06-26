x = int(input())

# 연산의 횟수를 저장 1~30000 총 30001개
cnt = [0] * 30001


def top(num):

    temp = 0
    if num == 1:
        return 0

    cnt[num] = top(num-1) + 1

    if num % 5 == 0:
        temp = top(num // 5) + 1
        if cnt[num] > temp:
            cnt[num] = temp

    if num % 3 == 0:
        temp = top(num // 3) + 1
        if cnt[num] > temp:
            cnt[num] = temp

    if num % 2 == 0:
        temp = top(num // 2) + 1
        if cnt[num] > temp:
            cnt[num] = temp

    return cnt[num]


top(x)

