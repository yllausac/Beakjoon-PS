n, m = map(int, input().split())
array = list(map(int, input().split()))


def search(x):
    max_x = min_x = array[0]
    cnt = 1
    for i in range(1, n):
        max_x = max(max_x, array[i])
        min_x = min(min_x, array[i])
        if max_x - min_x > x:
            cnt += 1
            max_x = array[i]
            min_x = array[i]
    return cnt


start, end = 0, max(array)
result = 0
while start <= end:
    mid = (start + end) // 2
    if search(mid) <= m:
        end = mid - 1
        result = mid
    else:
        start = mid + 1

print(result)
