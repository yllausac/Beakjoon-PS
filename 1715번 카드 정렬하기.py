import sys
import heapq

input = sys.stdin.readline
n = int(input())
card = []
for _ in range(n):
    card.append(int(input()))
heapq.heapify(card)
result = 0

while len(card) != 1:
    num1 = heapq.heappop(card)
    num2 = heapq.heappop(card)
    sum_ = num1 + num2
    result += sum_
    heapq.heappush(card, sum_)

print(result)


