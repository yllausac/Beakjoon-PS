dx = [0, 1, 2, 0, 1, 2, 0, 1, 2]
dy = [0, 0, 0, 1, 1, 1, 2, 2, 2]


def dfs(y, x, k):
    _init = p[y][x]

    if k == 1:
        result[_init] += 1
        return

    for i in range(y, y+k):
        for j in range(x, x+k):
            if p[i][j] != _init:
                for i in range(9):
                    s = k//3
                    nx = x + s*dx[i]
                    ny = y + s*dy[i]
                    dfs(ny, nx, s)
                return

    result[_init] += 1


n = int(input())
p = []
result = {-1: 0, 0: 0, 1: 0}

for _ in range(n):
    p.append(list(map(int, input().split())))

dfs(0, 0, n)

for i in range(-1, 2):
    print(result[i])
