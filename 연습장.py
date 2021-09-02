import sys

input = sys.stdin.readline
n = int(input())
posi, nega = [], []
result = 0
for _ in range(n):
    num = int(input())
    if num > 1:
        posi.append(num)
    elif num == 1:
        result += 1
    else:
        nega.append(num)

posi.sort(reverse=True)
nega.sort()

if len(posi) % 2 == 0:
    for i in range(0, len(posi), 2):
        result += posi[i] * posi[i+1]
else:
    for i in range(0, len(posi)-1, 2):
        result += posi[i] * posi[i+1]
    result += posi[len(posi)-1]

if len(nega) % 2 == 0:
    for i in range(0, len(nega), 2):
        result += nega[i] * nega[i+1]
else:
    for i in range(0, len(nega)-1, 2):
        result += nega[i] * nega[i+1]
    result += nega[len(nega)-1]

print(result)
