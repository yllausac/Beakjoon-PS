n = int(input())
lecture = []
queue = []
for _ in range(n):
    p, d = map(int, input().split())
    lecture.append([d, p])

lecture.sort()
for i in range(n):
    for j in range(i+1, n):
        if lecture[i][0] == lecture[j][0]:
            queue.append(lecture[i])


schedule = [x for x in lecture if x not in queue]
result = 0
for i in range(len(schedule)):
    result += schedule[i][1]
print(result)
