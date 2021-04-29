modi = input().split('-')
num = []

for i in modi:
    count = 0
    s = i.split('+')
    for j in s:
        count += int(j)
    num.append(count)

n = num[0]
for i in range(1, len(num)):
    n -= num[i]
print(n)

