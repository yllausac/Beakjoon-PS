while True:
    sentence = input()
    if sentence == ".":
        break
    sentence_stack = []
    answer = True

    for j in sentence:
        if j == "(" or j == "[":
            sentence_stack.append(j)

        elif j == ")":
            if len(sentence_stack) == 0:
                answer = False
                break
            if sentence_stack[-1] == "(":
                sentence_stack.pop()
            else:
                answer = False
                break
        elif j == "]":
            if len(sentence_stack) == 0:
                answer = False
                break
            if sentence_stack[-1] == "[":
                sentence_stack.pop()
            else:
                answer = False
                break

    if answer and not sentence_stack:
        print("yes")
    else:
        print("no")
