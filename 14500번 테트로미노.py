n, m = map(int, input().split())
paper = []
for _ in range(n):
    paper.append(list(map(int, input().split())))
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
result = 0
visit = [[0] * m for i in range(n)]
mfinger = [[[0, 1], [0, 2], [-1, 1]], [[0, 1], [0, 2], [1, 1]],
           [[1, 0], [2, 0], [1, 1]], [[1, 0], [1, -1], [2, 0]]]  # dfs로 갈 수 없는 모형이므로 따로 설정


def dfs(a, b, count, temp):
    global result
    if count == 4:
        result = max(result, temp)
        return
    for k in range(4):
        x, y = a + dx[k], b + dy[k]
        if 0 <= x < n and 0 <= y < m and visit[x][y] == 0:
            visit[x][y] = 1
            dfs(x, y, count + 1, temp + paper[x][y])
            visit[x][y] = 0


def middle(x, y):
    global result
    for i in mfinger:
        try:
            temp = paper[x][y] + paper[x + i[0][0]][y + i[0][1]] + paper[x + i[1][0]][y + i[1][1]] + paper[x + i[2][0]][y + paper[2][1]]
        except:
            temp = 0
        result = max(result, temp)


for i in range(n):
    for j in range(m):
        visit[i][j] = 1
        dfs(i, j, 1, paper[i][j])
        visit[i][j] = 0
        middle(i, j)

print(result)
