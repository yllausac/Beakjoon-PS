import sys
import heapq

input = sys.stdin.readline
n, m = map(int, input().split())
arr = [[]for i in range(n+1)]
indegree = [0] * (n+1)
heap, result = [], []

for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    indegree[b] += 1

for i in range(1, n+1):
    if indegree[i] == 0:
        heapq.heappush(heap, i)

while heap:
    data = heapq.heappop(heap)
    result.append(data)
    for j in arr[data]:
        indegree[j] -= 1
        if indegree[j] == 0:
            heapq.heappush(heap, j)
for i in result:
    print(i, end=' ')
