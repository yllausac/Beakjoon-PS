import sys

input = sys.stdin.readline
n, m, k = map(int, input().split())
l = []
tree = [0] * 3000000
for _ in range(n):
    l.append(int(input().rstrip()))


# 세그먼트 트리 생성
def init(node, start, end):
    if start == end:
        tree[node] = l[start]
        return tree[node]
    else:
        tree[node] = init(node*2, start, (start+end)//2) + init(node*2+1, (start+end)//2+1, end)
        return tree[node]

import sys

input = sys.stdin.readline
n = int(input())
budgets = list(map(int, input().split()))
budgets.sort()
m = int(input())


def binary_search(budgets):
    left = 0
    right = budgets[-1]

    while left <= right:
        mid = (left + right) // 2
        num = 0
        for budget in budgets:
            if budget >= mid:
                num += mid
            else:
                num += budget
        if num <= m:
            left = mid + 1
        else:
            right = mid - 1

    return right


print(binary_search(budgets))
