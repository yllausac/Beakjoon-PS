n = int(input())
array = list(map(int, input().split()))
sum_1 = [array[0]]

for i in range(n - 1):
    sum_1.append(max(sum_1[i] + array[i + 1], array[i + 1]))

print(max(sum_1))
