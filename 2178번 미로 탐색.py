n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))
dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]
queue = [[0, 0]]
graph[0][0] = 1
while queue:
    a, b = queue[0][0], queue[0][1]
    del queue[0]
    for i in range(4):
        x = a + dx[i]
        y = b + dy[i]
        if 0 <= x < n and 0 <= y < m and graph[x][y] == 1:
            queue.append([x, y])
            graph[x][y] = graph[a][b] + 1
print(graph[n-1][m-1])






