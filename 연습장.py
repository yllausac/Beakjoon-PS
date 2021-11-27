n, m = map(int, input().split())
room = []
dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]
for i in range(n):
    room.append(list(map(int, input())))
queue = []
count = 0

for i in range(n):
    for j in range(m):
            count = 0
            for x in range(i - 1, i + 2):
                for y in range(j - 1, j + 2):
                    if x < 0 or y < 0 or x >= n or y >= m:
                        continue

                    elif room[x][y] == 1:
                        count += 1


    print(count)