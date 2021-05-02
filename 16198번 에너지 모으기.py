n = int(input())
w = list(map(int, input().split()))


def E(w):
    if len(w) == 3:
        return w[0] * w[2]
    energe = 0
    for i in range(1, len(w)-1):
        r = w[i-1] * w[i+1] + E(w[:i] + w[i+1:])
        energe = max(energe, r)
    return energe


print(E(w))
