import sys

input = sys.stdin.readline
R, C = map(int, input().split())
graph = []
for _ in range(R):
    graph.append(list(input().rstrip()))
dx = [-1, 0, 1]
visit = [[False]*C for _ in range(R)]
ans = 0


def solve(i, j):
    if j == C-1:
        return True

    for d in dx:
        if 0 <= i + d < R and graph[i+d][j+1] == '.' and not visit[i+d][j+1]:
            visit[i+d][j+1] = True
            if solve(i+d, j+1):
                return True
    return False


for i in range(R):
    if graph[i][0] == '.':
        if solve(i, 0):
            ans += 1

print(ans)
