from collections import deque

n, m = map(int, input().split())
graph = []
for _ in range(m):
    graph.append(list(input()))
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
result = []
visit = [[-1]*n for i in range(m)]
visit[0][0] = 0
queue = deque()


def bfs(i, j):
    queue.append([0, 0])
    while queue:
        a, b = queue[0][0], queue[0][1]
        del queue[0]
        for k in range(4):
            x = a + dx[k]
            y = b + dy[k]
            if 0 <= x < m and 0 <= y < n and visit[x][y] == -1:
                if graph[x][y] == '0':
                    queue.appendleft([x, y])
                    visit[x][y] = visit[a][b]
                elif graph[x][y] == "1":
                    queue.append([x, y])
                    visit[x][y] = visit[a][b] + 1


bfs(0, 0)

print(visit[m-1][n-1])
