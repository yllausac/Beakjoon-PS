n, m = map(int, input().split())
dp = [i for i in range(n+1)]
print(dp)


def find(target):
    if target == dp[target]:
        return target

    dp[target] = find(dp[target])
    return dp[target]


def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        dp[b] = a
    else:
        dp[a] = b


for _ in range(m):
    flag, a, b = map(int, input().split())
    if flag:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
    else:
        union(a, b)
