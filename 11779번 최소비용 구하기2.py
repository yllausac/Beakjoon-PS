import sys
import heapq

input = sys.stdin.readline
INF = 1e9
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
dp = [INF] * (n+1)
heap = []
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))


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
                last_trace[next_node] = now
                heapq.heappush(heap, (next_wei, next_node))
    return record(start, end)


def record(start, end):
    res = [end]
    last_trace[start] = 0
    while last_trace[end]:
        res.append(last_trace[end])
        end = last_trace[end]
    return result(res[::-1])


def result(res):
    print(dp[end])
    print(len(res))
    print(*res)


start, end = map(int, input().split())
last_trace = [None] * (n+1)
Dijkstra(start)
