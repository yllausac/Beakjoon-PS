import sys


input = sys.stdin.readline
n = int(input())
num = list(map(int, input().split()))
num.sort()
m = int(input())
item = list(map(int, input().split()))


def binary_search(num, test):
    left = 0
    right = len(num) - 1

    while left <= right:
        mid = (left + right) // 2
        current_item = num[mid]
        if current_item == test:
            return 1
        else:
            if test < current_item:
                right = mid - 1
            else:
                left = mid + 1

    return 0


for test in item:
    print(binary_search(num, test))


