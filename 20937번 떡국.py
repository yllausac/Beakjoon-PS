N = int(input())
dduk = list(map(int, input().split()))

dduk.sort()
dduk.reverse()

for i in range(len(dduk) - 1):
