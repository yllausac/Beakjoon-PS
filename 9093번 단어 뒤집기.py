T = int(input())
for _ in range(T):
    sentence = input().split()
    for s in sentence:
        print(s[::-1], end=' ')
    print()
