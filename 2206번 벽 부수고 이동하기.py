import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().strip())))
dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]


def bfs():
    visit = [[0] * m for _ in range(n)]
    visit[0][0] = 1
    queue = deque()
    queue.append([0, 0])
    while queue:
        a, b = queue.popleft()
        if a == n-1 and b == m-1:
            return visit[a][b]
        for k in range(4):
            x = a + dx[k]
            y = b + dy[k]
            if 0 <= x < n and 0 <= y < m and visit[x][y] == 0:
                if graph[x][y] == 0:
                    visit[x][y] = visit[a][b] + 1
                    queue.append([x, y])

    return -1

result = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            graph[i][j] = 0
            if bfs() != -1:
                result.append(bfs())
            graph[i][j] = 1

if len(result) == 0:
    print(-1)
else:
    print(min(result))



