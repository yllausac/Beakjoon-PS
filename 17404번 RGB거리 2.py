from sys import maxsize

n = int(input())
RGB = [[0]*n for _ in range(n+1)]
for i in range(1, n+1):
    RGB[i][0], RGB[i][1], RGB[i][2] = map(int, input().split())
dp = [[0]*n for _ in range(n+1)]
INF = maxsize
result = INF


for first in range(3):
    for i in range(3):
        if first == i:
            dp[1][i] = RGB[1][i]
        else:
            dp[1][i] = INF

    for i in range(2, n+1):
        dp[i][0] = RGB[i][0] + min(dp[i-1][1], dp[i-1][2])
        dp[i][1] = RGB[i][1] + min(dp[i-1][0], dp[i-1][2])
        dp[i][2] = RGB[i][2] + min(dp[i-1][0], dp[i-1][1])

    for i in range(3):
        if i == first:
            continue
        result = min(result, dp[n][i])

print(result)
