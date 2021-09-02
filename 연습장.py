import sys
import heapq

input = sys.stdin.readline
n, k = map(int, input().split())
wei, val = [], []
gem = []
for _ in range(n):
    m, v = map(int, input().split())
    heapq.heappush(gem, [m, v])
bag = []
for _ in range(k):
    capacity = int(input())
    heapq.heappush(bag, capacity)

total_value = 0
capable_gem = []

for _ in range(k):
    capacity = heapq.heappop(bag)
    while gem and capacity >= gem[0][0]:
        [m, v] = heapq.heappop(gem)
        heapq.heappush(capable_gem, -v)
    if capable_gem:
        total_value -= heapq.heappop(capable_gem)
    elif not gem:
        break

print(total_value)
