import sys, copy

input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
ans = 0


def move(dir):
    if dir == 0:  # 위로 이동
        for j in range(n):
            idx = 0
            for i in range(1, n):
                if board[i][j]:  # 숫자가 있는 칸이면
                    temp = board[i][j]  # temp에 숫자 저장
                    board[i][j] = 0  # 0으로 바꿔줌
                    if board[idx][j] == 0:
                        board[idx][j] = temp
                    elif board[idx][j] == temp:
                        board[idx][j] = temp * 2
                        idx += 1
                    else:
                        idx += 1
                        board[idx][j] = temp
    elif dir == 1:  # 아래로 이동
        for j in range(n):
            idx = n - 1
            for i in range(n - 2, -1, -1):
                if board[i][j]:
                    temp = board[i][j]
                    board[i][j] = 0
                    if board[idx][j] == 0:
                        board[idx][j] = temp
                    elif board[idx][j] == temp:
                        board[idx][j] = temp * 2
                        idx -= 1
                    else:
                        idx -= 1
                        board[idx][j] = temp

    elif dir == 2:  # 좌로 이동
        for i in range(n):
            idx = 0
            for j in range(1, n):
                if board[i][j]:
                    temp = board[i][j]
                    board[i][j] = 0
                    if board[i][idx] == 0:
                        board[i][idx] = temp
                    elif board[i][idx] == temp:
                        board[i][idx] = temp * 2
                        idx += 1
                    else:
                        idx += 1
                        board[i][idx] = temp
    else:  # 우로 이동
        for i in range(n):
            idx = n - 1
            for j in range(n-2, -1, -1):
                if board[i][j]:
                    temp = board[i][j]
                    board[i][j] = 0
                    if board[i][idx] == 0:
                        board[i][idx] = temp
                    elif board[i][idx] == temp:
                        board[i][idx] = temp * 2
                        idx -= 1
                    else:
                        idx -= 1
                        board[i][idx] = temp


def dfs(cnt):
    global board, ans
    if cnt == 5:
        for i in range(n):
            for j in range(n):
                ans = max(ans, board[i][j])
        return
    temp_a = copy.deepcopy(board)
    for i in range(4):
        move(i)
        dfs(cnt + 1)
        board = copy.deepcopy(temp_a)


dfs(0)
print(ans)