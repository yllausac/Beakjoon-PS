n, s, d = map(int, input().split())
graph = []
for _ in range(n-1):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1
print(graph)
visited = [0]*n


def find(x):
    if parents[x] == x:
        return cnt
    if visited[x]:
        return cnt - 1
    cnt += 1
    if d < cnt:
        visited[x] = True
        return find(parents[x])

parents =

