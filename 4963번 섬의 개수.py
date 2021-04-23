dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, -1, 1, -1, -1, 1, 1]


def bfs(i, j):
    graph[i][j] = 0
    queue = [[i, j]]
    while queue:
        a, b = queue[0][0], queue[0][1]
        del queue[0]
        for k in range(8):
            x = a + dx[k]
            y = b + dy[k]
            if 0 <= x < h and 0 <= y < w and graph[x][y] == 1:
                graph[x][y] = 0
                queue.append([x, y])
    print()

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    graph = []
    component = 0
    for _ in range(h):
        graph.append(list(map(int, input().split())))
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                bfs(i, j)
                component += 1
    print(component)
