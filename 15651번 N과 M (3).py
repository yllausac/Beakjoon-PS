n, m = map(int, input().split())
number = [i for i in range(1, n+1)]
array = []


def dfs(x):
    if x == m:
        print(*array)
        return

    for i in number:
        array.append(i)
        dfs(x+1)
        array.pop()

dfs(0)