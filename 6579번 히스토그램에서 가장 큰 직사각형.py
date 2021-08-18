import sys

input = sys.stdin.readline
while True:
    n, *height = list(map(int, input().split()))
    if n == 0:
        break

    height.insert(0, 0)
    height += [0]
    checked = [0]
    area = 0

    for i in range(1, n+2):
        while checked and (height[checked[-1]] > height[i]):
            cur_height = checked.pop()
            area = max(area, (i-1-checked[-1])*height[cur_height])
        checked.append(i)
    print(area)
