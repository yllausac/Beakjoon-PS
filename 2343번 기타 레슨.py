import sys
n, m = map(int, input().split())
lesson = list(map(int, input().split()))
ans = sys.maxsize


left, right = max(lesson), sum(lesson)
while left <= right:
    mid = (left + right) // 2
    count = 0
    sum_ = 0
    for i in range(len(lesson)):
        if sum_ + lesson[i] > mid:
            count += 1
            sum_ = 0
        sum_ += lesson[i]
    if sum_:
        count += 1
    if count > m:
        left = mid + 1
    else:
        ans = min(ans, mid)
        right = mid - 1

print(ans)
