N = int(input())
row = []
count = 0
for i in range(N):
    row.append(str(input()))

for i in row:
    x = i
    h = i.count('H')
    t = i.count('T')
    if h < t:
        trans = str.maketrans('HT', 'TH')
        x = i.translate(trans)
        row.pop()
        row.append(x)
        count += 1

for i in range(N):
    for j in range(N):
        row[i][j]

print(row[1][2])
print(row)
print(count)