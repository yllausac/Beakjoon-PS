import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
before = [list(input().strip().split()) for _ in range(n)]
after = [list(input().strip().split()) for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def solv():
    for x in range(n):
        for y in range(m):
            if before[x][y] != after[x][y]:
                bfs(x, y)
                return check()
    return 'YES'


def bfs(x, y):
    global before
    visited = [[False] * m for _ in range(n)]
    queue = deque([(x, y)])

    visited[x][y] = True
    target = before[x][y]
    num = after[x][y]
    while queue:
        cx, cy = queue.pop()
        before[cx][cy] = num

        for k in range(4):
            nx = cx + dx[k]
            ny = cy + dy[k]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == False:
                if before[nx][ny] == target:
                    visited[nx][ny] = True
                    queue.appendleft((nx, ny))


def check():
    for x in range(n):
        for y in range(m):
            if before[x][y] != after[x][y]:
                return 'NO'
    return 'YES'


print(solv())
