from collections import deque

n, k = map(int, input().split())
visit = [0 for _ in range(100001)]

def bfs():
    queue = deque()
    queue.append(n)
    visit[n] = 1

    while queue:
        s = queue.popleft()
        if s == k:
            print(visit[s] - 1)
            break
        if 0 <= s-1 < 100001 and visit[s-1] == 0:
            visit[s-1] = visit[s] + 1
            queue.append(s-1)
        if 0 < 2*s < 100001 and visit[2*s] == 0:
            visit[2*s] = visit[s]
            queue.appendleft(2*s)
        if 0 <= s+1 < 100001 and visit[s+1] == 0:
            visit[s+1] = visit[s] + 1
            queue.append(s+1)

bfs()

