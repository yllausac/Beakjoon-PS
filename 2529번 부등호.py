k = int(input())
op = list(input().split())
c = [False] * 10  # 중복방지
max_k, min_k = "", ""


def possible(i, j, k):
    if k == "<":
        return i < j
    if k == ">":
        return i > j
    return True


def solve(count, s):
    global max_k, min_k
    if count == k + 1:  # 맨 처음 나타나는 값이 최소, 마지막 저장되는 값이 최대
        if len(min_k) == 0:
            min_k = s
        else:
            max_k = s
        return

    for i in range(10):
        if not c[i]:
            if count == 0 or possible(s[-1], str(i), op[count - 1]):
                c[i] = True
                solve(count + 1, s + str(i))
                c[i] = False


solve(0, "")
print(max_k)
print(min_k)