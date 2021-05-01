n = int(input())
graph = [[]*(n+1) for i in range(n+1)]
for _ in range(n):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visit = [[0]*(n+1) for i in range(n+1)]
isCycle = [False] * n
cycle = False
print(graph)
print(visit)


def dfs(x, start, length):
    global cycle
    if x == start and length >= 2:
        cycle = True
        return

    visit[x] = 1
    for i in graph[x]:
        if visit[i] == 0:
            dfs(i, start, length + 1)
        elif i == start and length >= 2:
            dfs(n, start, length)


for i in range(n+1):
    visit = [0] * (n+1)
    cycle = False
    dfs(i, i, 0)

    if cycle:
        isCycle[i] = True

print(isCycle)
