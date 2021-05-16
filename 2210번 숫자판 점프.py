graph = []
for _ in range(5):
    graph.append(list(map(str, input().split())))
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
number = []


def dfs(x, y, dp):
    if len(dp) == 6:
        if dp not in number:
            number.append(dp)
        return

    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < 5 and 0 <= ny < 5:
            dfs(nx, ny, dp + graph[nx][ny])


for i in range(5):
    for j in range(5):
        dfs(i, j, graph[i][j])

print(len(number))
