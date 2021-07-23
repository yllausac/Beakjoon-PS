import sys
import heapq

input = sys.stdin.readline
n, e = map(int, input().split())
INF = sys.maxsize
graph = [[] for _ in range(n+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
comp1, comp2 = map(int, input().split())


def Dijkstra(start):
    dp = [INF for i in range(n+1)]
    dp[start] = 0
    heap = []
    heapq.heappush(heap, [0, start])
    while heap:
        w, c = heapq.heappop(heap)
        for next_node, next_wei in graph[c]:
            wei = next_wei + w
            if dp[next_node] > wei:
                dp[next_node] = wei
                heapq.heappush(heap, [wei, next_node])
    return dp


one = Dijkstra(1)
comp1_ = Dijkstra(comp1)
comp2_ = Dijkstra(comp2)
# start -> comp1 -> comp2 -> n 의 경우와 start -> comp2 -> comp1 -> n 의 경우가 있다.
cnt = min(one[comp1] + comp1_[comp2] + comp2_[n], one[comp2] + comp2_[comp1] + comp1_[n])
print(cnt if cnt < INF else -1)
