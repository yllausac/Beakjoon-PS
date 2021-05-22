n, s, d = map(int, input().split())
graph = []
for _ in range(n-1):
    x = list(map(int, input().split()))
    graph.append(x)
print(graph)

def dfs(node, p):
    for