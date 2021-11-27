n, m = map(int, input().split())
room = []
dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]
for i in range(n):
    room.append(list(map(int, input())))
visit = [[0]*n for i in range(m)]
queue = []
count = 0
for i in range(n):
    for j in range(m):
        if room[i][j] == 1 and visit[i][j] == 0:
            queue.append([i, j])
            visit[i][j] = 1
            while queue:
                a, b = queue[0][0], queue[0][1]
                del queue[0]
                for k in range(4):
                    x = a + dx[k]
                    y = b + dy[k]
                    if 0 <= x < n and 0 <= y < m and room[x][y] == 1 and visit[x][y] == 0:
                        queue.append([x, y])
                        visit[i][j] = 1
                        count += 1

print(count)

