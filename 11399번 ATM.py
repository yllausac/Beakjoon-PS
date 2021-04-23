N = int(input())
time = list(map(int, input().split()))
time_sum = 0
time.sort()


for i in range(N):
    for j in range(i + 1):
        time_sum += time[j]

print(time_sum)

