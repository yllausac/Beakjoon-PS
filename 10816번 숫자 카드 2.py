n = int(input())
card = list(map(int, input().split()))
m = int(input())
check = list(map(int, input().split()))

card.sort()
num = dict()
for i in card:
    num.setdefault(i)
    num[i] = card.count(i)


def binary_search(n, card, start, end):
    if start > end:
        return 0
    m = (start+end)//2
    if n == card[m]:
        return card[start:end+1].count(n)
    elif n < card[m]:
        return binary_search(n, card, start, m-1)
    else:
        return binary_search(n, card, m+1, end)

n_dic = {}
for n in card:
    start = 0
    end = len(card) - 1
    if n not in n_dic:
        n_dic[n] = binary_search(n, card, start, end)

print(' '.join(str(n_dic[x]) if x in n_dic else '0' for x in check))