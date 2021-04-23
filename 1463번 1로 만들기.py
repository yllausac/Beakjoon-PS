n = int(input())

dp = [0 for _ in range(n+2)]
dp[2] = 1

for i in range(2, len(dp)):
    dp[i] = dp[i-1] + 1

    if i % 3 == 0:
        if dp[i] > dp[int(i/3)] + 1:
            dp[i] = dp[int(i/3)] + 1
    if i % 2 == 0:
        if dp[i] > dp[int(i / 2)] + 1:
            dp[i] = dp[int(i / 2)] + 1

print(dp[n])