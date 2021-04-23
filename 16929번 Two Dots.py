n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(input()))
dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]
visit = [[0]*m for _ in range(n)]
cycle = False


def dfs(init_a, init_b, a, b, count, color):
    global cycle
    if cycle:
        return
    visit[a][b] = 1

    if init_a == a and init_b == b and count >= 4:
        cycle = True
        return

    for k in range(4):
        x = a + dx[k]
        y = b + dy[k]

        if 0 <= x < n and 0 <= y < m:
            if visit[x][y] == 0 and color == graph[x][y]:
                dfs(init_a, init_b, x, y, count+1, color)
            elif x == init_a and y == init_b and count >= 4:
                dfs(init_a, init_b, x, y, count, color)
    return


for i in range(n):
    for j in range(m):
        visited = [[0]*m for _ in range(n)]
        visit[i][j] = 1
        dfs(i, j, i, j, 1, graph[i][j])

if cycle:
    print("Yes")
else:
    print("No")
