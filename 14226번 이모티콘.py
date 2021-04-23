from collections import deque

s = int(input())
screen = [[-1]*(s+1) for i in range(s+1)]
#  screen[화면에 나온 이모티콘 개수][클립보드의 이모티콘 개수]

def bfs():
    queue = deque()
    queue.append([1, 0])
    screen[1][0] = 0

    while queue:
        x, y = queue.popleft()

        if screen[x][x] == -1:  # 1번 연산
            screen[x][x] = screen[x][y] + 1
            queue.append([x, x])
        if x+y <= s and screen[x+y][y] == -1:  # 2번 연산
            screen[x+y][y] = screen[x][y] + 1
            queue.append([x+y, y])
        if x-1 >= 0 and screen[x-1][y] == -1:  # 3번 연산
            screen[x-1][y] = screen[x][y] + 1
            queue.append([x-1, y])

bfs()

result = screen[s][1]
for i in range(1, s):
    if screen[s][i] != -1:
        result = min(result, screen[s][i])

print(result)