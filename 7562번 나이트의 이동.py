from collections import deque

t = int(input())
dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]


def bfs(start_x, start_y, goal_x, goal_y):
    queue = deque()
    queue.append([start_x, start_y])
    graph[start_x][start_y] = 1
    while queue:
        a, b = queue.popleft()
        if a == goal_x and b == goal_y:
            print(graph[goal_x][goal_y] - 1)
            return
        for i in range(8):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < n and 0 <= y < n and graph[x][y] == 0:
                queue.append([x, y])
                graph[x][y] = graph[a][b] + 1

for _ in range(t):
    n = int(input())
    graph = [[0]*n for i in range(n)]
    start_x, start_y = map(int, input().split())
    goal_x, goal_y = map(int, input().split())
    bfs(start_x, start_y, goal_x, goal_y)