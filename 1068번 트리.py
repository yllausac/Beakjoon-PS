import sys

input = sys.stdin.readline
n = int(input())
s = list(map(int, input().split()))
d = int(input())
graph = [[0]*n for i in range(n)]
visit = [0 for _ in range(n)]
s_len = len(s)
cnt = 0
for i in range(s_len):
    if s[i] != -1:
        graph[i][s[i]] = 1
        graph[s[i]][i] = 1
    else:
        root = i
for i in range(n):
    graph[i][d] = 0
    graph[d][i] = 0


def dfs(root):
    global cnt
    isTrue = False
    visit[root] = 1
    for i in range(n):
        if graph[root][i] == 1 and visit[i] == 0:
            isTrue = True
            dfs(i)
    if not isTrue:
        cnt += 1


dfs(root)
if d == root:
    print(0)
else:
    print(cnt)
