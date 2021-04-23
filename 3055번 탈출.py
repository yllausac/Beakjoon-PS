from collections import deque


R, C = map(int, input().split())
graph = []
for _ in range(R):
    graph.append(list(input()))
print(graph)
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]


def bfs():
    queue_water = deque()
    queue_amurensis = deque()
    count = 0
    for i in range(R):
        for j in range(C):
            if graph[i][j] == "*":
                queue_water.append([i, j])
            if graph[i][j] == "S":
                queue_amurensis.append([i, j])

    while queue_water:
        a, b = queue_water.popleft()
        for k in range(4):
            x = a + dx[k]
            y = b + dy[k]
            if 0 <= x < R and 0 <= y < C and graph[x][y] == ".":
                queue_water.append([x, y])