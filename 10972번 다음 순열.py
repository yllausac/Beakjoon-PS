n = int(input())
array = list(map(int, input().split()))
x = 0

for i in range(n-1, 0, -1):
    if array[i-1] < array[i]:
        x = i - 1
        break

for i in range(n-1, 0, -1):
    if array[x] < array[i]:
        array[x], array[i] = array[i], array[x]
        array = array[:x+1] + sorted(array[x+1:])
        print(*array)
        exit()

print(-1)