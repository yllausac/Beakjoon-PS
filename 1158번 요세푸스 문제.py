N, K = map(int, input().split())
yo = [i for i in range(1, N+1)]
result = []
i = 0

while len(yo) != 0:
    i = i + K
    if i > len(yo):
        i = i % len(yo)
        if i == 0:
            i = i + len(yo)
    i = i-1
    result.append(yo.pop(i))

result_str = [str(a) for a in result]
print("<",end='')
print(", ".join(result_str),end='')
print(">",end='')