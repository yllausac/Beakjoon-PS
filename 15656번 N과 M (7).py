n, m = map(int, input().split())
number = list(map(int, input().split()))

number.sort()
answer = []


def solve(count, n, m):
    if count == m:
        print(' '.join(map(str, answer)))
        return
    for i in range(n):
        answer.append(number[i])
        solve(count + 1, n, m)
        answer.pop()


solve(0, n, m)
