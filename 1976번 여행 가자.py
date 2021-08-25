import sys

input = sys.stdin.readline
n = int(input())
m = int(input())
parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i


def find(a):
    if a == parent[a]:
        return a
    p = find(parent[a])
    parent[a] = p
    return parent[a]


def union(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for y in range(1, n+1):
    graph = list(map(int, input().split()))
    for x in range(1, len(graph)+1):
        if graph[x-1] == 1:
            union(y, x)

plan = list(map(int, input().split()))
result = set([find(city) for city in plan])
if len(result) != 1:
    print('NO')
else:
    print('YES')
