n, m = map(int, input().split())
money = list(map(int, input().split()))

dp = [10001]*(m+1) # 최댓값으로 dp 채워넣음
dp[0] = 0


for i in money:
    for j in range(i, m+1):
        if dp[j-i] != 10001:
            dp[j] = min(dp[j], dp[j-i]+1)


if dp[m] == 10001:
    print(-1)
else:
    print(dp[m])