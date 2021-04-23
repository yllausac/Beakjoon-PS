n = int(input())
rc = list(map(int, input().split()))
start = [rc[0], rc[1]]
goal = [rc[2], rc[3]]
dx, dy = [-2, -2, 0, 0, 2, 2], [-1, 1, -2, 2, -1, 1]
queue = []
visit = [[0]*n for _ in range(n)]


def bfs(i, j, goal_i, goal_j):
    queue.append([i, j])
    visit[i][j] = 1
    while queue:
        a, b = queue[0][0], queue[0][1]
        del queue[0]
        if a == goal_i and b == goal_j:
            print(visit[goal_i][goal_j] - 1)
            return
        for k in range(6):
            x = a + dx[k]
            y = b + dy[k]
            if 0 <= x < n and 0 <= y < n and visit[x][y] == 0:
                queue.append([x, y])
                visit[x][y] = visit[a][b] + 1
    print(-1)


bfs(start[0], start[1], goal[0], goal[1])
