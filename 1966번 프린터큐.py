t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    imp = list(map(int, input().split()))
    idx = [0 for i in range(n)]
    idx[m] = 1
    cnt = 0
    while True:
        if imp[0] == max(imp):
            cnt += 1
            if idx[0] == 1:
                print(cnt)
                break
            else:
                del imp[0]
                del idx[0]
        else:
            imp.append(imp[0])
            del imp[0]
            idx.append(idx[0])
            del idx[0]
