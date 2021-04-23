n = int(input())
tree = {i: [] for i in range(1, n+1)}
weight = {i: [0] for i in range(1, n+1)}
visit = [0 for i in range(n+1)]
depth = [0 for i in range(n+1)]


for _ in range(n-1):
    parent, child, w = map(int, input().split())
    tree[parent].append(child)
    weight[child].append(w)


def dfs(v, tree, visit):
    visit[v] = 1
    for child in tree[v]:
        if visit[child] == 0:
            depth[child] += weight[child][-1]
            dfs(child, tree, visit)


for i in range(1, n+1):
    visit = [0 for i in range(n+1)]
    dfs(i, tree, visit)


print(max(depth))