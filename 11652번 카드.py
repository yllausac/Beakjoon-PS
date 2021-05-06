n = int(input())
card = {}
for _ in range(n):
    tmp = int(input())
    if tmp in card:
        card[tmp] += 1
    else:
        card[tmp] = 1

card = sorted(card.items(), key=lambda x: (-x[1], x[0]))

print(card[0][0])
