n = int(input())
consul = []
for _ in range(n):
    t, p = map(int, input().split())
    consul.append([t, p])
dp = [0 for i in range(n+1)]

for i in range(n-1, -1, -1):
    if i + consul[i][0] > n:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(consul[i][1] + dp[i + consul[i][0]], dp[i+1])

print(dp[0])