n = int(input())
state = list(map(int, input()))
goal = list(map(int, input()))


def switch(x):
    if x == 0:
        x = 1
    else:
        x = 0
    return x


def click(state, cnt):
    count = cnt
    if count == 1:
        state[0] = switch(state[0])
        state[1] = switch(state[1])
    for i in range(1, n):
        if state[i - 1] != goal[i - 1]:
            count += 1
            state[i - 1] = switch(state[i - 1])
            state[i] = switch(state[i])
            if i != n - 1:
                state[i + 1] = switch(state[i + 1])
    if state == goal:
        return count
    else:
        return -1


res1 = click(state[:], 0)  # 시작할 때 스위치를 누른다
res2 = click(state[:], 1)  # 시작할 때 스위치를 안누른다
if res1 >= 0 and res2 >= 0:
    print(min(res1, res2))
elif res1 >= 0 and res2 < 0:
    print(res1)
elif res1 < 0 and res2 >= 0:
    print(res2)
else:
    print(-1)
