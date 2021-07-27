import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for i in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))
start, end = map(int, input().split())
_min, _max = 1, 1e9


def Dijkstra(c):
    queue = deque()
    queue.append(start)
    visited = set()
    visited.add(start)
    result = []
    while queue:
        y = queue.popleft()
        for w, x in graph[y]:
            if x not in visited and w >= c:
                visited.add(x)
                queue.append(x)
    return True if end in visited else False


result = _min
while _min <= _max:
    mid = (_min + _max) // 2
    if Dijkstra(mid):
        result = mid
        _min = mid + 1
    else:
        _max = mid - 1
print(int(result))
