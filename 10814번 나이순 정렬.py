n = int(input())
member = []*n

for _ in range(n):
    old, name = map(str, input().split())
    member.append([old, name])

member.sort(key=lambda x: int(x[0]))
for i in range(n):
    print(member[i][0], member[i][1])

