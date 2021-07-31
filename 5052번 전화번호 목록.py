import sys


input = sys.stdin.readline
t = int(input())
endFlag = False
for _ in range(t):
    n = int(input())
    book = list(input().rstrip() for _ in range(n))
    book.sort()

    for i in range(len(book) - 1):
        if book[i] in book[i+1][:len(book[i])]:
            print('NO')
            endFlag = True
            break
    if endFlag == False:
        print('YES')
    endFlag = False
