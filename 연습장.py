import heapq

n, k = map(int, input().split())
gem = []
for _ in range(n):
    m, v = map(int, input().split())
    heapq.heappush(gem, [m, v])  # gem에다가 [m, v]를 넣음

bag = []
for _ in range(k):
    capacity = int(input())
    heapq.heappush(bag, capacity)  # bag에다 capacity를 넣음

total_value = 0
capable_gem = []

for _ in range(k):
    capacity = heapq.heappop(bag)  # bag의 최솟값을 heappop
    while gem and capacity >= gem[0][0]:  # 현재 bag의 capacity보다 이하인 모든 보석
        [m, v] = heapq.heappop(gem)  # 최소 무게부터 꺼낸다
        heapq.heappush(capable_gem, -v)  # 무게를 제외한 값만 heappush하여 넣어준다
    if capable_gem:  # gem 최소보다는 작지만 넣을 수 있는 보석은 있는 경우
        total_value -= heapq.heappop(capable_gem)
    elif not gem:  # 남은 보석이 없는 경우
        break

print(total_value)





