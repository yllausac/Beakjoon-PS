from collections import deque

R, C = map(int, input().split())
graph = []
for _ in range(R):
    graph.append(list(input()))
print(graph)
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
visit = [[0] * C for i in range(R)]


def bfs():
    queue_water = deque()
    queue_amurensis = deque()
    queue_beaver = deque()
    for i in range(R):
        for j in range(C):
            if graph[i][j] == "*":
                queue_water.append([i, j])
            if graph[i][j] == "S":
                queue_amurensis.append([i, j])
                visit[i][j] = 1
            if graph[i][j] == "D":
                queue_beaver.append([i, j])

    while queue_water and queue_amurensis:
        a, b = queue_water.popleft()
        c, d = queue_amurensis.popleft()
        if graph[c][d] == "D":
            print(visit[c][d] - 1)
            exit()
        for k in range(4):
            x = a + dx[k]
            y = b + dy[k]
            nx = c + dx[k]
            ny = d + dy[k]

            if x == queue_beaver[0][0] and y == queue_beaver[0][1]:  # 물의 움직임
                continue
            if 0 <= x < R and 0 <= y < C and graph[x][y] == ".":
                queue_water.append([x, y])
                graph[x][y] = "*"

            if 0 <= nx < R and 0 <= ny < C and visit[nx][ny] == 0:  # 고슴도치의 움직임
                if graph[nx][ny] != "X" and graph[nx][ny] != "*":
                    queue_amurensis.append([nx, ny])
                    visit[nx][ny] = visit[c][d] + 1

    print(-1)

bfs()