n = int(input())
graph = []
for _ in range(n):
    graph.append(list(input()))
dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]
visit = [[0]*n for i in range(n)]
queue = []



def bfs(i, j):
    queue.append([i, j])
    visit[i][j] = 1
    while queue:
        a, b = queue[0][0], queue[0][1]
        del queue[0]
        for k in range(4):
            x = a + dx[k]
            y = b + dy[k]
            if 0 <= x < n and 0 <= y < n and visit[x][y] == 0:
                if graph[x][y] == graph[a][b]:
                    queue.append([x, y])
                    visit[x][y] = 1

# 일반인의 경우
block = 0
for i in range(n):
    for j in range(n):
        if visit[i][j] == 0:
            bfs(i, j)
            block += 1
print(block, end=' ')

# 적록색약화
for i in range(n):
    for j in range(n):
        if graph[i][j] == "R":
            graph[i][j] = "G"

# visit 초기화
visit = [[0]*n for _ in range(n)]

# 적록색약의 경우
block = 0
for i in range(n):
    for j in range(n):
        if visit[i][j] == 0:
            bfs(i, j)
            block += 1
print(block)