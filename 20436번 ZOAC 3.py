L_start, R_start = input().split()
word = list(input())
left_time, right_time = 0, 0
time = left_time + right_time
q, w, e, r, t, a, s, d, f, g, z, x, c, v = (0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (0, -1), (1, -1), (2, -1), (3, -1), (4, -1), (0,-2),(1,-2),(2,-2),(3,-2)
y, u, i, o, p, h, j, k, l, b, n, m = (5,0),(6,0),(7,0),(8,0),(9,0),(5,-1),(6,-1),(7,-1),(8,-1),(4,-2),(5,-2),(6,-2)

left_keyboard = []
right_keyboard = []
for i in word:
    if i in ["q","w","e","r","t","a","s","d","f","g","z","x","c","v"]:
        left_keyboard.append(i)
    else:
        right_keyboard.append(i)

print(z)
print(z[1])
for i in left_keyboard:
    print(i[0])
