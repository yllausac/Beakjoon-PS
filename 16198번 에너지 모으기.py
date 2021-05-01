n = int(input())
w = list(map(int, input().split()))
energe = 0

for i in range(1, n):
    energe = max(w[i] + w[i+1], energe)


print(energe)
