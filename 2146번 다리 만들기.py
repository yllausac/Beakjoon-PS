import sys
from collections import deque


def grouping(i, j):  # 섬마다 번호 붙이기
    q = deque([(i, j)])
    world[i][j] = gid
    while q:
        qi, qj = q.popleft()
        for t in range(4):
            x, y = qi + dx[t], qj + dy[t]
            if 0 <= x < n and 0 <= y < n:
                if world[x][y] == 1:
                    world[x][y] = gid
                    q.append((x, y))
                elif world[x][y] == 0 and not (qi, qj) in ocean:
                    ocean.append((qi, qj))


def get_distance():  # 모든 섬에서 동시에 확장
    loop = 0
    ans = sys.maxsize  # 변수가 취할 수 있는 최댓값.
    while ocean:
        loop += 1
        for _ in range(len(ocean)):
            oi, oj = ocean.popleft()
            for t in range(4):
                x, y = oi + dx[t], oj + dy[t]
                if 0 <= x < n and 0 <= y < n:
                    if world[x][y] == 0:
                        world[x][y] = world[oi][oj]
                        ocean.append((x, y))
                    elif world[x][y] < world[oi][oj]:
                        # 이미 다리가 연결되었지만 다음 간척사업을 진행하던 중 알게된 경우.
                        ans = min(ans, (loop - 1) * 2)
                    elif world[x][y] > world[oi][oj]:
                        # 중복된 곳에 간척사업을 하게되는 경우
                        ans = min(ans, loop * 2 - 1)
    return ans


dx, dy = (0, 0, 1, -1), (1, -1, 0, 0)
n = int(sys.stdin.readline())
world = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
ocean = deque()
gid = -1
for i in range(n):
    for j in range(n):
        if world[i][j] > 0:
            grouping(i, j)
            gid -= 1  # 섬들끼리 구분짓기 위하여 반복문이 한번 돌 때마다 -1, -2, -3으로 줄여준다.

sys.stdout.write(str(get_distance()))
