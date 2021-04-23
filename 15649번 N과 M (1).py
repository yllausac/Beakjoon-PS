n, m = map(int, input().split())
number = [_ for _ in range(1, n+1)]
check = [False] * n  # 중복방지
array = []


def dfs(x):
    if x == m:
        print(*array)
        return

    for i in range(n):
        if check[i]:  # check[i]가 True 이면 패스한다.
            continue  # 즉, 중복될 경우 패스한다.

        array.append(number[i])
        check[i] = True

        dfs(x + 1)

        array.pop()
        check[i] = False


dfs(0)
