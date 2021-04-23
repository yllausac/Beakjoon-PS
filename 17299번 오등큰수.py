import sys

n = int(input())
array = list(map(int, sys.stdin.readline().split()))
F = []
stack = []
ans = [-1 for _ in range(n)]

for i in array:
    F.append(array.count(i))

for i in range(len(F)):
    while stack and F[stack[-1]] < F[i]:
        ans[stack.pop()] = array[i]
    stack.append(i)

print(*ans)


