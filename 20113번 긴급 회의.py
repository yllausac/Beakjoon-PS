from collections import Counter

N = int(input())
vote = list(map(int, input().split()))
while 0 in vote:
    vote.remove(0)
if len(vote) == 0:
    print("skipped")
    quit()

def modefinder(numbers):
    c = Counter(numbers)
    order = c.most_common()
    maximum = order[0][1]

    modes = []
    for num in order:
        if num[1] == maximum:
            modes.append(num[0])
    return modes

x = list(map(int, modefinder(vote)))

if len(x) == 1:
    print(*x)
else:
    print("skipped")



#중학생 풀이...
a = int(input())
b = [0]+list(map(int, input().split()))
c = [0]*(a+1)
for i in b:
    if i == 0:
        continue
    c[i] += 1
m = max(c)
if c.count(m) > 1:
    print('skipped')
else:
    print(c.index(m))
