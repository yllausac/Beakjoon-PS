from copy import deepcopy
n, m = map(int, input().split())


def fill(x, y, office, direction):
    for k in direction:
        nx, ny = x, y
        while True:
            nx += dx[k]
            ny += dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                if office[nx][ny] == 6:
                    break
                elif office[nx][ny] == 0:
                    office[nx][ny] = "#"
            else:
                break


def dfs(office, cnt):
    global result
    temp = deepcopy(office)
    if cnt == cctv_cnt:
        num = 0
        for i in range(n):
            num += temp[i].count(0)
        result = min(result, num)
        return
    x, y, cctv = queue[cnt]
    for i in direction[cctv]:
        fill(x, y, temp, i)
        dfs(temp, cnt + 1)
        temp = deepcopy(office)


dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
direction = [[], [[0], [1], [2], [3]], [[0, 1], [2, 3]], [[3, 0], [0, 2], [2, 1], [1, 3]],
[[1, 3, 0], [3, 0, 2], [0, 2, 1], [2, 1, 3]], [[0, 1, 2, 3]]]
cctv_cnt = 0
result = 100000000
office = []
queue = []
for i in range(n):
    a = list(map(int, input().split()))
    office.append(a)
    for j in range(len(a)):
        if a[j] != 0 and a[j] != 6:
            queue.append([i, j, a[j]])
            cctv_cnt += 1

dfs(office, 0)
print(result)

