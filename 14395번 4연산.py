import sys
from collections import deque

input = sys.stdin.readline
s, t = map(int, input().split())
queue = deque()
check = set()
queue.append((s, ''))
check.add(s)
MAX = 10e9

if s == t:
    print(0)
else:
    res = -1
    while queue:
        current_number, oper = queue.popleft()
        if current_number == t:
            res = oper
            print(res)
            exit(0)

        next_number = current_number * current_number
        if 0 <= next_number <= MAX and next_number not in check:
            queue.append((next_number, oper + '*'))
            check.add(next_number)

        next_number = current_number + current_number
        if 0 <= next_number <= MAX and next_number not in check:
            queue.append((next_number, oper + '+'))
            check.add(next_number)

        next_number = 1
        if next_number not in check:
            queue.append((next_number, oper + '/'))
            check.add(next_number)
    print(res)
