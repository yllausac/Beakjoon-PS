k, n = map(int, input().split())
lan = []
for _ in range(k):
    lan.append(int(input()))
lan.sort()
start, end = 1, lan[-1]


while start <= end:
    mid = (start + end) // 2  # 중간위치
    count = 0  # 랜선 수
    for i in lan:
        count += i // mid  # 분할된 랜선 수

    if count >= n:
        start = mid + 1
    else:
        end = mid - 1
print(end)
