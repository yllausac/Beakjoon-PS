import sys

r, c = map(int, sys.stdin.readline().strip().split())
graph = []
for _ in range(r):
    graph.append(list(sys.stdin.readline()))
record = []
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]


def dfs(a, b, count):
    global result
    result = max(count, result)
    record.append(graph[0][0])
    for k in range(4):
        x, y = a + dx[k], b + dy[k]
        if 0 <= x < r and 0 <= y < c and (graph[x][y] not in record):
            record.append(graph[x][y])
            dfs(x, y, count + 1)
            record.remove(graph[x][y])


result = 1
dfs(0, 0, result)
print(result)
