import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(v, stem):
    visit[v] = 1
    if stem >= 4:
        print("1")
        exit()
    for i in graph[v]:
        if visit[i] == 0:
            dfs(i, stem + 1)


for i in range(n):
    visit = [0 for i in range(n)]
    dfs(i, 0)

print(0)
