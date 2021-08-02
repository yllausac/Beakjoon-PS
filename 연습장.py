n = 10
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tree = [0] * (n*4)


def init(start, end, index):
    if start == end:
        tree[index] = array[start]
        return tree[index]
    mid = (start + end) // 2
    tree[index] = init(start, mid, index*2) + init(mid+1, end, index*2+1)


def query(start, end, index, qleft, qright):
    if qleft > end or qright < start:
        return 0
    if qleft <= start and end <= qright:
        return tree[index]
    mid = (start+end)//2
    return query(start, mid, index*2, qleft, qright) + query(mid+1, end, index*2+1, qleft,qright)


init(1, n, 1)
s, e = map(int, input().split())
print(query(1, n, 1, s, e))
