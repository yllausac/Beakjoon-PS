import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)
n = int(input())
m = int(input())

dp = [INF]*(n+1)
heap = []
graph = [[]for _ in range(n+1)]


def Dijkstra(start):
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


for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))
start, end = map(int, input().split())

Dijkstra(start)
print(dp[end])
