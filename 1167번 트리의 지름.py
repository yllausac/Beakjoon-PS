import sys
from collections import deque

input = sys.stdin.readline
v = int(input())
graph = [[] for _ in range(v+1)]
for _ in range(v):
    c = list(map(int, input().split()))
    for e in range(1, len(c)-2, 2):
        graph[c[0]].append((c[e], c[e+1]))


def bfs(start):
    visit = [-1] * (v+1)
    queue = deque()
    queue.append(start)
    visit[start] = 0
    _max = [0, 0]

    while queue:
        t = queue.popleft()
        for e, w in graph[t]:
            if visit[e] == -1:
                visit[e] = visit[t] + w
                queue.append(e)
                if _max[0] < visit[e]:
                    _max = visit[e], e
    return _max


dis, node = bfs(1)
dis, node = bfs(node)
print(dis)
