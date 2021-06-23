n, m, x, y, k = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

order = list(map(int, input().split()))
dice = [0, 0, 0, 0, 0, 0, 0] # 헷갈리므로 0번째는 0으로 놓고 7개를 만든다.


def move(dir):
    if dir == 1:
        dice[1], dice[3], dice[4], dice[6] = dice[3], dice[6], dice[1], dice[4]
    elif dir == 2:
        dice[1], dice[3], dice[4], dice[6] = dice[4], dice[1], dice[6], dice[3]
    elif dir == 3:
        dice[1], dice[2], dice[5], dice[6] = dice[2], dice[6], dice[1], dice[5]
    elif dir == 4:
        dice[1], dice[2], dice[5], dice[6] = dice[5], dice[1], dice[6], dice[2]


def dire(dir):  # x, y좌표를 이동시키기 위함
    if dir == 1: return 0, 1
    elif dir == 2: return 0, -1
    elif dir == 3: return -1, 0
    elif dir == 4: return 1, 0


for i in order:
    a, b = dire(i)
    if 0 <= x + a < n and 0 <= y + b < m:
        x += a
        y += b
        move(i)
        if board[x][y] != 0:
            dice[1] = board[x][y]
            board[x][y] = 0
        else:
            board[x][y] = dice[1]
        print(dice[6])
