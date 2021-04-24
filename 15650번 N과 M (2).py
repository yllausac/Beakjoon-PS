n, m = map(int, input().split())
number = [i for i in range(1, n+1)]
check = [False] * n
array = []


def dfs(x):
    if x == m:
        print(*array)
        return

    for i in range(n):
        if check[i]:
            continue
        if len(array) > 0 and array[-1] > number[i]:
            continue

        else:
            array.append(number[i])
            check[i] = True

            dfs(x+1)

            array.pop()
            check[i] = False

dfs(0)