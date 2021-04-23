L = list(input())
bomb = list(input())
stack = []

for i in L:
    stack.append(i)
    if i == bomb[-1] and stack[-len(bomb):] == bomb:
        del stack[-len(bomb):]

if len(stack) == 0:
    print("FRULA")
else:
    print("".join(stack))