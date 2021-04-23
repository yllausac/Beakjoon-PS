n, m = map(int, input().split())
graph_a, graph_b = [], []
cnt = 0

for _ in range(n):
    graph_a.append(list(map(int, input())))
for _ in range(n):
    graph_b.append(list(map(int, input())))


for i in range(n):
    for j in range(m):
        if graph_a[i][j] != graph_b[i][j]:
            for x in range(i, i + 3):
                for y in range(j, j + 3):
                    graph_a[x][y] = 1 - graph_a[x][y]
            cnt += 1
        elif i == n-3 and j == m-2:
            break
            print(-1)

print(cnt)


