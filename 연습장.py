from copy import deepcopy

n = int(input())
s = []
for _ in range(n):
    s.append(list(map(int, input().split())))


def dif(start):
    global result
    link = []
    for i in range(n):
        if i in start:
            continue
        link.append(i)
    start_n = 0
    link_n = 0
    for i in range(n//2 - 1):
        for j in range(i+1, n // 2):
            a, b = start[i], start[j]
            c, d = link[i], link[j]
            start_n += s[a][b] + s[b][a]
            link_n += s[c][d] + s[d][c]
    result = min(result, abs(start_n - link_n))


def dfs(temp):
    t = deepcopy(temp)
    if len(t) == n//2:
        dif(t)
        return
    for i in range(t[-1] + 1, n):
        t.append(i)
        dfs(t)
        t.pop()


result = 1000000000
temp = [0]
dfs(temp)
print(result)

