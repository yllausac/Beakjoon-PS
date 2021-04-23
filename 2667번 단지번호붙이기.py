n = int(input())
graph = []
dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]
for i in range(n):
    graph.append(list(map(int, input())))
component = []


def bfs(i, j):
    graph[i][j] = 0
    queue = [[i, j]]
    count = 1
    while queue:
        a, b = queue[0][0], queue[0][1]
        del queue[0]
        for k in range(4):
            x = a + dx[k]
            y = b + dy[k]
            if 0 <= x < n and 0 <= y < n and graph[x][y] == 1:
                graph[x][y] = 0
                queue.append([x, y])
                count += 1
    component.append(count)

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            bfs(i, j)
component.sort()
print(len(component))
for i in component:
    print(i)