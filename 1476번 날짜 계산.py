E, S, M = map(int, input().split())
i = 1
while True:
    e = i % 15
    if e == 0:
        e = 15
    s = i % 28
    if s == 0:
        s = 28
    m = i % 19
    if m == 0:
        m = 19
    if E == e and S == s and M == m:
        print(i)
        break
    i += 1
