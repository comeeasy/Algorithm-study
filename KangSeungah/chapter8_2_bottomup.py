x = int(input())

# 연산의 횟수를 저장 1~30000 총 30001개(0포함)
cnt = [0] * 30001

for i in range(2, x+1):

    # d
    cnt[i] = cnt[i-1] + 1

    # a
    if i % 5 == 0:
        if cnt[i] > cnt[i // 5] + 1:
            cnt[i] = cnt[i // 5] + 1

    # b
    if i % 3 == 0:
        if cnt[i] > cnt[i // 3] + 1:
            cnt[i] = cnt[i // 3] + 1

    # c
    if i % 2 == 0:
        if cnt[i] > cnt[i // 2] + 1:
            cnt[i] = cnt[i // 2] + 1


print(cnt[x])

