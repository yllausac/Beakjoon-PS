k, n = map(int, input().split())
lan = []
for _ in range(k):
    lan.append(int(input()))
lan.sort()
start, end = 1, lan[-1]


while start <= end:
    mid = (start + end) // 2
    count = 0
    for i in lan:
        count += i // mid

    if count >= n:
        start = mid + 1
    else:
        end = mid - 1
print(end)
