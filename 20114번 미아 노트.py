N, H, W = list(map(int, input().split()))
word = [[0 for _ in range(H)] for _ in range(W)]
result = ""
jj = 0
for i in range(H):
    word[i] = list(input())

while True:
    if len(result) == N:
        break
    asd = "?"
    for i in range(H):
        know = False
        if know == True:
            break
        for j in range(jj, jj+W):
            if word[i][j] != "?":
                asd = word[i][j]
                know = True
                break
    result += asd
    jj += W

print(result)



