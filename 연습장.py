import sys

input = sys.stdin.readline
n = int(input())
word = []
for _ in range(n):
    word.append(list(input().rstrip()))
alpha_dict = {}
num = []

for i in range(n):
    for j in range(len(word[i])):
        if word[i][j] in alpha_dict:
            alpha_dict[word[i][j]] += 10 ** (len(word[i])-j-1)
        else:
            alpha_dict[word[i][j]] = 10 ** (len(word[i])-j-1)

for val in alpha_dict.values():
    num.append(val)

num.sort(reverse=True)

sum = 0
idx = 9
for i in num:
    sum += idx * i
    idx -= 1

print(sum)




