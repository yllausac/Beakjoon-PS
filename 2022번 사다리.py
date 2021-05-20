import math

x, y, c = map(float, input().split())
left, right = 0, min(x, y)

while (abs(right-left) > 1e-6):  # abs는 절댓값을 반환한다.
    mid = (left + right) / 2.0
    d = mid
    h1 = math.sqrt(x*x - d*d)  # sqrt는 제곱근을 반환한다.
    h2 = math.sqrt(y*y - d*d)
    h = (h1*h2) / (h1+h2)
    if h > c:
        left = mid
    else:
        right = mid

print("%.3f"%round(mid, 3))  # round는 반올림해주는 함수.
