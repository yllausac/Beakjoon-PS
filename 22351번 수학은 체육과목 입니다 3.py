import sys

input = sys.stdin.readline
s = input().strip()


def solv():
    if len(s) < 4:
        target = s[0]
        flag = True
        for n in s[1:]:
            if target != n:
                flag = False
                break
        if flag:
            print(s, s)
            return

    for start in range(1, 1000):
        temp_str = str(start)
        if temp_str[0] == s[0]:
            temp_str = ''
            for end in range(start, 1000):
                temp_str += str(end)
                if len(temp_str) == len(s):
                    if temp_str == s:
                        print(start, end)
                        return
                    else:
                        break


solv()
