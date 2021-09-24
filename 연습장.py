import sys

input = sys.stdin.readline
n, k = map(int, input().split())
number = list(map(int, input().strip()))
result = []
delnum = k

for i in range(n):
    while delnum > 0 and result:
        if result[-1] < number[i]:
            result.pop()
            delnum -= 1
        else:
            break
    result.append(number[i])

for i in range(n-k):
    print(result[i], end='')


