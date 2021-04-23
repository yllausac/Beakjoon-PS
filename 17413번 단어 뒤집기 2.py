from collections import deque

S = list(input())
stack_1 = []
stack_2 = deque()
state = True
answer = ""

for i in S:
    if i == "<":
        while stack_1:
            answer += stack_1.pop()
        stack_2.append(i)
        state = False
    elif i == ">":
        stack_2.append(i)
        state = True
        while stack_2:
            answer += stack_2.popleft()
    elif i == " ":
        if state:
            while stack_1:
                answer += stack_1.pop()
            answer += " "
        else:
            stack_2.append(i)
            while stack_2:
                answer += stack_2.popleft()
    else:
        if state:
            stack_1.append(i)
        else:
            stack_2.append(i)
while stack_1:
    answer += stack_1.pop()

print(answer)

