import sys

input = sys.stdin.readline
n = int(input())
pen = list(map(int, input().split()))
pen.sort()
target = 1
for x in pen:
    if target < x:
        break
    target += x

print(target)
