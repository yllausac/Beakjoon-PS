n = int(input())
number = list(map(int, input().split()))
operator = list(map(int, input().split()))
max_result = -1000000001
min_result = 1000000001


def dfs(count, result, p, m ,mul, div):
    global max_result
    global min_result
    if count == n:
        max_result = max(max_result, result)
        min_result = min(min_result, result)
        return
    if p:
        dfs(count+1, result+number[count], p-1, m, mul, div)
    if m:
        dfs(count + 1, result - number[count], p, m - 1, mul, div)
    if mul:
        dfs(count + 1, result * number[count], p, m, mul - 1, div)
    if div:
        dfs(count + 1, -(-result // number[count]) if result < 0 else result // number[count], p, m, mul, div - 1)


dfs(1, number[0], operator[0], operator[1], operator[2], operator[3])
print(max_result)
print(min_result)