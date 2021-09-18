import sys

input = sys.stdin.readline
r, c = map(int, input().split())
graph = []
for _ in range(r):
    graph.append(list(input()))
dx = [-1, 0, 1]
visit = [[False]*c for _ in range(r)]
ans = 0


def solve(i, j):
    if j == c - 1:
        return True

    for d in dx:
        if 0 <= i + d < r and graph[i+d][j+1] == '.' and not visit[i+d][j+1]:
            visit[i+d][j+1] = True
            if solve(i+d, j+1):
                return True
    return False


for i in range(r):
    if graph[i][0] == '.':
        if solve(i, 0):
            ans += 1

print(ans)
