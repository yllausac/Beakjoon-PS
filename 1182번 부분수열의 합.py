n, s = map(int, input().split())
number = list(map(int, input().split()))
count = 0


def dfs(idx, sum):
    global count
    if idx >= n:
        return
    sum += number[idx]
    if sum == s:
        count += 1
    dfs(idx + 1, sum - number[idx])
    dfs(idx + 1, sum)


dfs(0, 0)
print(count)