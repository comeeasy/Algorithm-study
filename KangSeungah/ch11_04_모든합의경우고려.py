from itertools import combinations

n = int(input())
won = list(map(int, input().split()))
won.sort()

money = [0]

for i in won:
    money[i] = i

for k in range(1, len(won)+1):
    a = list(combinations(won, k))
    for i in range(len(a)):
        index = sum(a[i])
        money[index] = index

# input값
# 5
# 3 2 1 1 9

# money 리스트
# [0, 1, 2, 3, 4, 5, 6, 7, 0, 9, 10, 11, 12, 13, 14, 15, 16]

# 1 ~ money리스트의 마지막 값까지 확인했을 때
# 처음으로 0값이 나오는

for i in range(1, len(money)+1):
    if money[i] == 0:
        print(i)
        break


