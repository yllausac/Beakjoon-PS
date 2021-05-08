from collections import deque

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]


def bfs(x, y, shark, time, eat):
    queue, can_eat = deque(), []
    queue.append([x, y])
    visit = [[0]*n for _ in range(n)]
    visit[x][y] = time
    while queue:
        qlen = len(queue)
        while qlen:
            x, y = queue.popleft()
            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == 0:
                    if graph[nx][ny] == 0 or graph[nx][ny] == shark:
                        visit[nx][ny] = visit[x][y] + 1
                        queue.append([nx, ny])
                    elif 0 < graph[nx][ny] < shark:
                        can_eat.append([nx, ny])
            qlen -= 1

        if can_eat:
            nx, ny = min(can_eat)
            eat += 1
            if eat == shark:
                eat = 0
                shark += 1
            graph[nx][ny] = 0
            return nx, ny, shark, visit[x][y] + 1, eat

    print(time)
    exit()


for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            x, y = i, j
            graph[i][j] = 0

shark, time, eat = 2, 0, 0
while True:
    x, y, shark, time, eat = bfs(x, y, shark, time, eat)
