import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr_int = {}
arr_name = {}
for i in range(n):
    poketmon = input()
    arr_int[i+1] = poketmon
    arr_name[poketmon] = i+1

for _ in range(m):
    order = input()
    if order.isdigit():
        print(arr_int[int(order)])
    else:
        print(arr_name[order])
