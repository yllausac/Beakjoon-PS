def dfs(start, count):
    if count == 6:
        for i in range(6):
            print(combi[i], end=' ')
        print()
        return
    for i in range(start, len(testcase)):
        combi[count] = testcase[i]
        dfs(i+1, count + 1)

combi = [0 for i in range(13)]

while True:
    testcase = list(map(int, input().split()))
    if testcase[0] == 0:
        break
    del testcase[0]
    dfs(0, 0)
    print()
