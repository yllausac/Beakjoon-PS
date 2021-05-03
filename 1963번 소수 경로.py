from collections import deque

e = [True for i in range(10001)]  # 1부터 10000까지 모든 수로 그래프를 만든다.
for i in range(2, 101):
    if e[i]:
        j = i * 2
        while j < 10001:
            e[j] = False
            j += i  # 소수는 모두 True 가 된다.


def bfs():
    queue = deque()
    queue.append([start, 0])
    visit = [0 for _ in range(10000)]  # 중복방지
    visit[start] = 1
    while queue:
        num, count = queue.popleft()
        if num == goal:
            return count
        if num < 1000:  # 1000미만은 허용x 이므로
            continue
        for i in [1, 10, 100, 1000]:
            n = num - num % (i*10)//i * i
            for _ in range(10):
                if visit[n] == 0 and e[n]:  # 방문x 이고 소수이면
                    visit[n] = 1
                    queue.append([n, count + 1])
                n += i


t = int(input())
for i in range(t):
    start, goal = map(int, input().split())
    result = bfs()
    print(result if result is not None else "Impossible")
