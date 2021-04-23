n = int(input())
meeting = []
for _ in range(n):
    meeting.append(list(map(int, input().split())))

meeting = sorted(meeting, key=lambda meeting: meeting[0])
meeting = sorted(meeting, key=lambda meeting: meeting[1])


count = 0
queue = 0
for i, j in meeting:
    if i >= queue:
        count += 1
        queue = j
print(count)