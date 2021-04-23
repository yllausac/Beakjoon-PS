from collections import deque

n, m = map(int, input().split())
graph = [0] * 101
pointer = [0] * 101

ladder = dict()
for _ in range(n):
    x, y = map(int, input().split())
    ladder[x] = y

snake = dict()
for _ in range(m):
    x, y = map(int, input().split())
    snake[x] = y

print(ladder)
print(snake)

def bfs():
    queue = deque([1])
    graph[1] = 1
    while queue:
        a = queue.popleft()

        for dice in range(1, 7):
            x = a + dice
            if 0 < x <= 100 and graph[x] == 0:
                if x in ladder.keys():
                    x = ladder[x]
                if x in snake.keys():
                    x = snake[x]
                if graph[x] == 0:
                    queue.append(x)
                    graph[x] = 1
                    pointer[x] = pointer[a] + 1

bfs()
print(pointer[100])



