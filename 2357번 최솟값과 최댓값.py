import sys

input = sys.stdin.readline

n, m = map(int, input().split())
num = []
for _ in range(n):
    num.append(int(input()))

for _ in range(m):
    a, b = map(int, input().split())
    result1 = max(num[a:b])
    result2 = min(num[a:b])

    print(result2, end=' ')
    print(result1)
