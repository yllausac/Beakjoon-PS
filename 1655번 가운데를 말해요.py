import sys
import heapq

input = sys.stdin.readline
n = int(input())
left, right = [], []
# 가운데 값을 찾아야 하므로 왼쪽의 가장 큰 수와 오른쪽의 가장 작은 수를 비교
for _ in range(n):
    x = int(input())
    if len(left) == len(right):
        heapq.heappush(left, (-x, x))
    else:
        heapq.heappush(right, (x, x))

    # 왼쪽 원소중 오른쪽보다 큰 값이 들어가 있을 경우 교환해줌
    if right and left[0][1] > right[0][1]:
        left_value = heapq.heappop(left)[1]
        right_value = heapq.heappop(right)[1]
        heapq.heappush(right, (left_value, left_value))
        heapq.heappush(left, (-right_value, right_value))

    print(left[0][1])
