import sys

input = sys.stdin.readline
g = int(input())
p = int(input())
gate = [False] * g
result = 0

for _ in range(p):
    plane = int(input())
    if not gate[plane-1]:
        gate[plane-1] = True
        result += 1
    else:
        pass

print(result)

