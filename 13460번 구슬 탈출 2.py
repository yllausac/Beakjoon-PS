from collections import deque

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(input()))
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
visit = [[[[False]*m for i in range(n)] for i in range(m)]for i in range(n)]
queue = deque()


for i in range(n):
    for j in range(m):
        if graph[i][j] == 'R':
            Ri, Rj = i, j
        if graph[i][j] == 'B':
            Bi, Bj = i, j
        if graph[i][j] == 'O':
            Oi, Oj = i, j

queue.append([Ri, Rj, Bi, Bj, 1])
visit[Ri][Rj][Bi][Bj] = True


def move(i, j, dx, dy):
    count = 0
    while graph[i+dx][j+dy] != '#' and graph[i][j] != 'O':
        i += dx
        j += dy
        count += 1
    return i, j, count


def bfs():
    while queue:
        Ri, Rj, Bi, Bj, d = queue.popleft()
        if d > 10:
            print(-1)
            exit()
        for k in range(4):
            nRi, nRj, Rc = move(Ri, Rj, dx[k], dy[k])
            nBi, nBj, Bc = move(Bi, Bj, dx[k], dy[k])
            if graph[nBi][nBj] != 'O':
                if graph[nRi][nRj] == 'O':
                    print(d)
                    return
                if nRi == nBi and nRj == nBj:
                    if Rc > Bc:
                        nRi -= dx[k]
                        nRj -= dy[k]
                    else:
                        nBi -= dx[k]
                        nBj -= dy[k]
                if not visit[nRi][nRj][nBi][nBj]:
                    visit[nRi][nRj][nBi][nBj] = True
                    queue.append([nRi, nRj, nBi, nBj, d+1])
    print(-1)

bfs()
