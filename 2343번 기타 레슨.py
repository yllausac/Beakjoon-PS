import sys
n, m = map(int, input().split())
time = list(map(int, input().split()))
ans = sys.maxsize


left, right = max(time), sum(time)
while left <= right:
    mid = (left + right) // 2
    count = 0
    sum_ = 0
    for i in range(len(time)):
        if sum_ + time[i] > mid:
            count += 1
            sum_ = 0
        sum_ += time[i]
    if sum_:
        count += 1
    if count > m:
        left = mid + 1
    else:
        ans = min(ans, mid)
        right = mid - 1

print(ans)
