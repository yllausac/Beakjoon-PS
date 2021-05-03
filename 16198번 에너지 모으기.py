n = int(input())
w = list(map(int, input().split()))


def E(w):
    if len(w) == 3:
        return w[0] * w[2]
    energe = 0
    for i in range(1, len(w)-1):
        r = w[i-1] * w[i+1] + E(w[:i] + w[i+1:])  # 기준으로부터 양변의 값을 곱하고 기준점을 제외한 리스트의 값을 더함
        energe = max(energe, r)
    return energe


print(E(w))
