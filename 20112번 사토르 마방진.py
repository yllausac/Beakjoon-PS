N = int(input())
word = []
for i in range(N):
    word.append(list(input()))

word_mirror = [['' for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        word_mirror[j][i] = word[i][j]

if word == word_mirror:
    print("YES")
else:
    print("NO")
