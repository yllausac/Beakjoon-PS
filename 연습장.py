n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())
count = 0

for i in a:
    if b > i:
        count += 1
    else:
        ans = b
        count += 1
        while ans < i:
            ans += c
            count += 1

print(count)