n, m = map(int, input().split())
number = [i for i in range(1, n+1)]
array = []


def dfs(x):
    if x == m:
        print(*array)
        return

    for i in range(n):
        if len(array) > 0 and array[-1] > number[i]:
            continue

        else:
            array.append(number[i])
            dfs(x+1)
            array.pop()


dfs(0)