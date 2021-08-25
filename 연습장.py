import sys

input = sys.stdin.readline
n = int(input())
m = int(input())
parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i


def find(a):  # a 노드의 부모노드 찾기
    if a == parent[a]:
        return a
    p = find(parent[a])
    parent[a] = p
    return parent[a]


def union(a, b):  # a집합과 b집합 합치기
    a = find(a)
    b = find(b)
    if a == b:
        return  # 동일한 집합이면 연결시에 순환이 발생
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for y in range(1, n+1):  # y번째 도시
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


