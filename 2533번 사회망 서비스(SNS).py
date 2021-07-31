import sys

sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline
n = int(input())
graph = [[]for _ in range(n+1)]
for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
visit = [0 for _ in range(n+1)]
dp = [[0, 0] for _ in range(n+1)]


def adapter(node):
    visit[node] = 1
    dp[node][0] = 1
    for i in graph[node]:
        if visit[i] == 0:
            adapter(i)
            dp[node][0] += min(dp[i][0], dp[i][1])
            dp[node][1] += dp[i][0]


adapter(1)
print(min(dp[1][0], dp[1][1]))
