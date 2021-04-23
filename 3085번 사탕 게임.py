def check(graph, s_row, e_row, s_col, e_col):
    result = 1
    # 행 체크
    for i in range(s_row, e_row + 1):
        count = 1
        for j in range(1, len(graph)):
            if graph[i][j - 1] == graph[i][j]:  # 아래쪽과 같다면
                count += 1
            else:
                count = 1
            if count > result:
                result = count
    # 열 체크
    for i in range(s_col, e_col + 1):
        count = 1
        for j in range(1, len(graph)):
            if graph[j - 1][i] == graph[j][i]:  # 오른쪽과 같다면
                count += 1
            else:
                count = 1
            if count > result:
                result = count
    return result


n = int(input())
graph = [list(input()) for _ in range(n)]
result = 0

for i in range(n):
    for j in range(n):
        if j < n-1:
            graph[i][j], graph[i][j+1] = graph[i][j+1], graph[i][j]  # 좌우교환
            temp = check(graph, i, i, j, j+1)  # 연속부분 체크
            if temp > result:
                result = temp
            graph[i][j], graph[i][j+1] = graph[i][j+1], graph[i][j]  # 원위치
        if i < n-1:
            graph[i][j], graph[i+1][j] = graph[i+1][j], graph[i][j]  # 상하교환
            temp = check(graph, i, i+1, j, j)  # 연속부분 체크
            if temp > result:
                result = temp
            graph[i][j], graph[i+1][j] = graph[i+1][j], graph[i][j]  # 원위치

print(result)