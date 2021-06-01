n = int(input())
k = int(input())

left = 1
right = k

while left <= right:
    mid = (left + right) // 2
    temp = 0
    for i in range(1, n+1):
        temp += min(mid//i, n)
    if temp >= k:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)
