a, b, c = map(int, input().split())
point = min(a, b, c)
if point == a:
    print("GO SANG")
elif point == b:
    print("GO HAN")
else:
    print("GO JUNG")
