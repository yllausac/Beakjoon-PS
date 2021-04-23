N, K = map(int, input().split())
A = []
for i in range(N):
    A.append(int(input()))
A.sort()
A.reverse()
coin = 0

for i in range(len(A)):
    coin += K // A[i]
    K %= A[i]

print(coin)