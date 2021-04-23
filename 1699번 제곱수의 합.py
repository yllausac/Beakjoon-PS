n = int(input())
array = []
result = []
for i in range(1, n):
    array.append(i*i)
array.reverse()

i = 0
while n != 0:
    while i < len(array):
        if (n - array[i]) >= 0:
            n = n - array[i]
            result.append(array[i])
            i = 0
        else:
            i += 1

print(len(result))
