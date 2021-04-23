pipe = list(input())
stack = []
result = 0

for i in range(len(pipe)):
    if pipe[i] == "(":
        stack.append("(")
    else:
        if pipe[i-1] == "(":
            stack.pop()
            result += len(stack)
        else:
            stack.pop()
            result += 1

print(result)
