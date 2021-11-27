from itertools import permutations
from itertools import combinations

n, k = map(int, input().split())
word = []
for i in range(n):
    word.append(list(input()))

word_ = []
word_.append(list(permutations(word, k)))
ori = []
new = []
for i in range(k):
    ori.append(word_[0][i][0])
    new.append(word_[0][i][-1])

ori_ = []
ori_.append(list(combinations(ori, k)))
new_ = []
new_.append(list(permutations(new, k)))


for i in ori_[0][0]:
    for j in new_[0][0]:
        if i == j:
            print("YES")
            exit()

print("NO")