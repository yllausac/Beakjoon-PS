import sys

input = sys.stdin.readline
n, k = map(int, input().split())
number = list(map(int, input().rstrip()))
result = []

for i in range(n):
    while k > 0 and result:
        if result[len(result)-1] < number[i]:
            result.pop()
            k -= 1
        else:
            break
    result.append(number[i])

for i in range(len(result)):
    print(result[i], end='')

