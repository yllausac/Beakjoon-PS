import sys
from collections import deque

input = sys.stdin.readline
t = int(input())

errflag = False
for i in range(t):
    p = input()
    n = int(input())
    arr = input()[1:-2].split(',')

    if arr[0] != '':
        arr = deque(arr)
    else:
        arr = deque()

    flag = True

    for func in p:
        if func == 'R':
            if flag == True:
                flag = False
            elif flag == False:
                flag = True
        elif func == 'D':
            if len(arr) == 0:
                print('error')
                errflag = True
                break
            if flag == True:
                arr.popleft()
            elif flag == False:
                arr.pop()
    if p.count('R') % 2 != 0:
        arr.reverse()

    if errflag == False:
        print('[', end='')
        for i in range(len(arr)):
            print(arr[i], end='')
            if i != len(arr) - 1:
                print(',', end='')
        print(']')
    errflag = False
