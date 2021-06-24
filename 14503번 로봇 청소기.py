n, m = map(int, input().split())
r, c, d = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def clean(x, y, d):
    global count
    if board[x][y] == 0:
        board[x][y] = 2
        count += 1
    for _ in range(4):
        nd = (d + 3) % 4
        nx = x + dx[nd]
        ny = y + dy[nd]
        if board[nx][ny] == 0:
            clean(nx, ny, nd)
            return
        d = nd
    nd = (d + 2) % 4
    nx = x + dx[nd]
    ny = y + dy[nd]
    if board[nx][ny] == 1:
        return
    clean(nx, ny, d)  # 방향은 유지하고 뒤로 이동하므로 d는 그대로


count = 0
clean(r, c, d)
print(count)
