import sys
import heapq


input = sys.stdin.readline
dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]
cnt = 1


def bfs():
    dp = [[1e9] * n for _ in range(n)]
    dp[0][0] = graph[0][0]
    visit = [[0] * n for _ in range(n)]
    heap = []
    heapq.heappush(heap, [graph[0][0], 0, 0])
    while heap:
        c, a, b = heapq.heappop(heap)
        for k in range(4):
            x = a + dx[k]
            y = b + dy[k]
            if 0 <= x < n and 0 <= y < n and visit[x][y] == 0:
                dp[x][y] = min(dp[x][y], dp[a][b] + graph[x][y])
                heapq.heappush(heap, [dp[x][y], x, y])
                visit[x][y] = 1
    return dp[n-1][n-1]


while True:
    n = int(input())
    if n == 0:
        break
    graph = []
    for i in range(n):
        graph.append(list(map(int, input().split())))
    result = bfs()
    print("Problem %d: %d" % (cnt, result))
    cnt += 1
