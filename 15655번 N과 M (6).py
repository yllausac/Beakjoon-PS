n, m = map(int, input().split())
number = list(map(int, input().split()))
number.sort()
array = []
check = [False]*n


def dfs(x):
    if x == m:
        print(*array)
        return

    for i in range(n):
        if len(array) > 0 and array[-1] > number[i]:
            continue
        if check[i] == False:
            array.append(number[i])
            check[i] = True
            dfs(x+1)
            array.pop()
            check[i] = False

dfs(0)

