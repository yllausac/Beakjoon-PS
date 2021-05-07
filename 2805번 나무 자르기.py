n, m = map(int, input().split())
tree = list(map(int, input().split()))


def treeSum(height):
    result = 0
    for i in tree:
        if i - height > 0:
            result += i - height

    return result


def binarySearch(target):
    start, end = 0, max(tree)
    ans = 0
    while start <= end:
        mid = (start + end)
        result = treeSum(mid)
        if result < target:
            end = mid - 1
        if result >= target:
            ans = mid
            start = mid + 1

    return ans


print(binarySearch(m))
