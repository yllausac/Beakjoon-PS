import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize
V, E = map(int, input().split())
k = int(input())
# 가중치 테이블 dp
dp = [INF]*(V+1)
heap = []
graph = [[]for _ in range(V+1)]


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


for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))

Dijkstra(k)
for i in range(1, V+1):
    print("INF" if dp[i] == INF else dp[i])
