n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
max_result = 0


def bfs():
    global max_result
    copy = [[0]*m for i in range(n)]
    for i in range(n):
        for j in range(m):
            copy[i][j] = graph[i][j]
    result = 0
    queue = []
    for i in range(n):
        for j in range(m):
            if copy[i][j] == 2:
                queue.append([i, j])
    while queue:
        a, b = queue[0][0], queue[0][1]
        del queue[0]
        for k in range(4):
            x = a + dx[k]
            y = b + dy[k]
            if 0 <= x < n and 0 <= y < m:
                if copy[x][y] == 0:
                    copy[x][y] = 2
                    queue.append([x, y])
    for i in copy:
        for j in i:
            if j == 0:
                result += 1  # 바이러스가 퍼지지 않은 곳을 세어줌
    max_result = max(max_result, result)  # 벽을 다른곳에 세웠을 때랑 비교해서 최대값만 남겨줌


def wall(count):
    if count == 3:
        bfs()  # 벽을 3개 세우면 바이러스를 퍼트려준다.
        return
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                wall(count + 1)
                graph[i][j] = 0

wall(0)
print(max_result)
