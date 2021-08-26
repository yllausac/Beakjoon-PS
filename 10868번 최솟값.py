import sys
from math import *

input = sys.stdin.readline
n, m = map(int, input().split())
num = []
for _ in range(n):
    num.append(int(input()))
h = int(ceil(log2(n)))
t_size = 1 << (h + 1)
tree = [0] * t_size


def init(start, end, index):
    if start == end:
        tree[index] = num[start]
        return tree[index]
    mid = (start + end) // 2
    tree[index] = min(init(start, mid, index*2), init(mid+1, end, index*2 + 1))
    return tree[index]


def query(start, end, index, qleft, qright):
    if start > qright or end < qleft:
        return 10000000001
    if qleft <= start and end <= qright:
        return tree[index]
    mid = (start + end) // 2
    return min(query(start, mid, index*2, qleft, qright), query(mid+1, end, index*2+1, qleft, qright))


init(0, n-1, 1)

for _ in range(m):
    a, b = map(int, input().split())
    print(query(0, n-1, 1, a-1, b-1))
