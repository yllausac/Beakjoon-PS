import sys
import heapq

input = sys.stdin.readline
n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input().rstrip())))
visit = [[0] * n for _ in range(n)]


def Dijkstra():
    dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]
    heap = []
    heapq.heappush(heap, [0, 0, 0])
    visit[0][0] = 1
    while heap:
        a, x, y = heapq.heappop(heap)
        if x == n - 1 and y == n - 1:
            print(a)
            return
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and  0 <= ny < n and visit[nx][ny] == 0:
                visit[nx][ny] = 1
                if graph[nx][ny] == 0:
                    heapq.heappush(heap, [a+1, nx, ny])
                else:
                    heapq.heappush(heap, [a, nx, ny])


Dijkstra()
