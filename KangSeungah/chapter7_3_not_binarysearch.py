n, m = list(map(int, input().split(' ')))

len_of_ddeok = list(map(int, input().split()))

# 각 떡을 1cm씩 자르는 행위를 세는 cnt
cnt = 0

while True:
    for j in range(n):
        if len_of_ddeok[j] > 0:
            len_of_ddeok[j] -= 1

    if sum(len_of_ddeok) < m:
        break

    cnt += 1

print(cnt)