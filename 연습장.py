import sys
import heapq

input = sys.stdin.readline
INF = 1e9
n, m, x = map(int, input().split())
graph = [[]for _ in range(n+1)]


def Dijkstra(start):
    heap = []
    dp = [INF]*(n+1)
    dp[start] = 0
    heapq.heappush(heap, (0, start))

    while heap:
        wei, now = heapq.heappop(heap)
        if dp[now] < wei:
            continue
        for w, next_node in graph[now]:
            next_wei = w + wei
            if next_wei < dp[next_node]:
                dp[next_node] = next_wei
                heapq.heappush(heap, (next_wei, next_node))
    return dp


for _ in range(m):
    u, v, t = map(int, input().split())
    graph[u].append((t, v))

result = 0
for i in range(1, n+1):
    go = Dijkstra(i)
    back = Dijkstra(x)
    result = max(result, go[x] + back[i])


print(result)