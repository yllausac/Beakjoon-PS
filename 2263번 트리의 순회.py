n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
idx = [0]*(n+1)


def pre_order(in_l, in_r, post_l, post_r):
    if in_l > in_r or post_l > post_r:
        return  # 역전되면 구분할 노드가 없는 것

    root = postorder[post_r]
    print(root, end=' ')

    left = idx[root] - in_l  # 왼쪽 개수
    right = in_r - idx[root]  # 오른쪽 개수

    pre_order(in_l, in_l + left - 1, post_l, post_l + left - 1)
    pre_order(in_r - right + 1, in_r, post_r - right, post_r - 1)


for i in range(n):
    idx[inorder[i]] = i  # post order의 끝 값이 inorder의 어디 인덱스에 위치한지 확인을 위해

pre_order(0, n-1, 0, n-1)
