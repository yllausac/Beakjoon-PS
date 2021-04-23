import sys

sys.setrecursionlimit(10001)
n, m = map(int, sys.stdin.readline().split())
graph = [[0]*(n+1) for i in range(n+1)]
visit = [0 for i in range(n+1)]
component = 0

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u][v] = 1
    graph[v][u] = 1


def dfs(v):
    visit[v] = 1
    for i in range(1, n+1):
        if visit[i] == 0 and graph[v][i] == 1:
            dfs(i)


for i in range(1, n+1):
    if visit[i] == 0:
        dfs(i)
        component += 1

print(component)
