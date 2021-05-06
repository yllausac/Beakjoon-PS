n = int(input())


def star(x, y):
    while x != 0:
        if x % 3 == 1 and y % 3 == 1:
            print(' ', end='')
            return None
        x = x//3
        y = y//3
    print("*", end='')


for i in range(n):
    for j in range(n):
        star(i, j)
    print('\n')
