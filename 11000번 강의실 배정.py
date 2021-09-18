import sys
import heapq

input = sys.stdin.readline
n = int(input())
class_ = []
for _ in range(n):
    s, t = map(int, input().split())
    class_.append([s, t])
class_.sort()

room = []
heapq.heappush(room, class_[0][1])

for i in range(1, n):
    if class_[i][0] < room[0]:
        heapq.heappush(room, class_[i][1])
    else:
        heapq.heappop(room)
        heapq.heappush(room, class_[i][1])

print(len(room))
