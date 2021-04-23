n, L = map(int, input().split())
x = list(map(int, input().split()))
result = True
s = 0

for i in range(n - 1, 0, -1):
    s += x[i]
    if x[i - 1] - L < s / (n - i) < x[i - 1] + L:
        result = True
    else:
        result = False
        break

if result == True:
    print('stable')
else:
    print('unstable')
