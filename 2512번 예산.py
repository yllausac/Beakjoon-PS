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
