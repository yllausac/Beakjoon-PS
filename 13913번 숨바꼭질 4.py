from collections import deque
import sys

n, k = map(int, sys.stdin.readline().split())
queue = deque()
queue.append([n, 0])
visit = [0]*100001
path = []


while queue:
    p, count = queue.popleft()
    if p == k:
        idx = p
        while idx != n:
            path.append(idx)
            idx = visit[idx]
        path.append(n)
        print(count)
    if p - 1 >= 0 and visit[p-1] == 0:
        queue.append([p-1, count+1])
        visit[p-1] = p

    if p + 1 <= 100000 and visit[p+1] == 0:
        queue.append([p+1, count+1])
        visit[p+1] = p

    if p*2 <= 100000 and visit[p*2] == 0:
        queue.append([p*2, count+1])
        visit[p*2] = p

print(*path[::-1])