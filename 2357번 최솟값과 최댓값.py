from math import *
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
num = []
for _ in range(n):
    num.append(int(input()))
h = int(ceil(log2(n)))
t_size = 1 << (h+1)
tree_Min = [0]*t_size
tree_Max = [0]*t_size


def init_Min(start, end, index):
    if start == end:
        tree_Min[index] = num[start]
        return tree_Min[index]
    mid = (start + end) // 2
    tree_Min[index] = min(init_Min(start, mid, index*2), init_Min(mid+1, end, index*2 + 1))
    return tree_Min[index]


def init_Max(start, end, index):
    if start == end:
        tree_Max[index] = num[start]
        return tree_Max[index]
    mid = (start + end) // 2
    tree_Max[index] = max(init_Max(start, mid, index*2), init_Max(mid+1, end, index*2 + 1))
    return tree_Max[index]


def query_Min(start, end, index, qleft, qright):
    if start > qright or end < qleft:
        return 1000000001
    if qleft <= start and end <= qright:
        return tree_Min[index]
    mid = (start + end) // 2
    return min(query_Min(start, mid, index*2, qleft, qright), query_Min(mid+1, end, index*2+1, qleft, qright))


def query_Max(start, end, index, qleft, qright):
    if start > qright or end < qleft:
        return 0
    if qleft <= start and end <= qright:
        return tree_Max[index]
    mid = (start + end) // 2
    return max(query_Max(start, mid, index*2, qleft, qright), query_Max(mid+1, end, index*2+1, qleft, qright))


init_Min(0, n-1, 1)
init_Max(0, n-1, 1)

for _ in range(m):
    a, b = map(int, input().split())
    print(query_Min(0, n-1, 1, a-1, b-1), end=' ')
    print(query_Max(0, n-1, 1, a-1, b-1))
