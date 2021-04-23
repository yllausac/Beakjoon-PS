N = int(input())
stack = []

import sys


def push(x):
    stack.append(x)


def pop():
    if (not stack):
        return -1
    else:
        return stack.pop()


def size():
    return len(stack)


def empty():
    return 0 if stack else 1


def top():
    return stack[-1] if stack else -1


for _ in range(N):
    input_split = sys.stdin.readline().rstrip().split()

    order = input_split[0]

    if order == "push":
        push(input_split[1])
        # push 1 이라고 입력했을 때, 1을 넣어주기 위함.
    elif order == "pop":
        print(pop())
    elif order == "size":
        print(size())
    elif order == "empty":
        print(empty())
    elif order == "top":
        print(top())
