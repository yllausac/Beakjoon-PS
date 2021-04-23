from collections import deque
m, n = map(int, input().split())
box = []
dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]
for _ in range(n):
    box.append(list(map(int, input().split())))
queue = deque()


def bfs():
    while queue:
        a, b = queue.popleft()
        for k in range(4):
            x = a + dx[k]
            y = b + dy[k]
            if 0 <= x < m and 0 <= y < n and box[x][y] == 0:
                box[x][y] = box[a][b] + 1
                queue.append([x, y])

for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            queue.append([i,j])
bfs()
isTrue = False
result = -2
for i in box:
    for j in i:
        if j == 0:
            isTrue = True
        result = max(result, j)
if isTrue == True:
    print(-1)
elif result == -1:
    print(0)
else:
    print(result - 1)