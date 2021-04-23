K = int(input())
stack = []


def push(x):
    stack.append(x)


def pop():
    stack.pop()


for _ in range(K):
    num = int(input())
    pop() if num == 0 else push(num)

print(sum(stack))