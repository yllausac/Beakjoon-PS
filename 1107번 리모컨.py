N = input()
n = list(map(int, N))
m = int(input())
remote = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
out = list(map(int, input().split()))
for i in range(len(out)):
    remote.remove(out[i])
print(remote)
stack = []
move = 0
for i in range(len(n)):
    j = 0
    if n[i] in remote:
        stack.append(n[i])
    else:
        while not (n[i] - j in remote or n[i] + j in remote):
            j += 1
        move += j


only_move = int(N) - 100
button_move = len(stack) + move + 1

print(min(button_move, only_move))



