n, r, c = map(int, input().split())
result = 0


def zet(n, x, y):
    global result
    if x == r and y == c:
        print(int(result))
        exit(0)

    if n == 1:
        result += 1
        return

    if not (x <= r < x + n and y <= c < y + n):
        result += n*n
        return
    zet(n/2, x, y)
    zet(n/2, x, y+n/2)
    zet(n/2, x+n/2, y)
    zet(n/2, x+n/2, y+n/2)


zet(2**n, 0, 0)
