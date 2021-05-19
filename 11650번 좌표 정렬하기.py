n = int(input())
cor = []
for _ in range(n):
    cor.append(list(map(int, input().split())))
cor.sort()
for i in range(n):
    for j in range(2):
        print(cor[i][j], end=' ')
    print()
