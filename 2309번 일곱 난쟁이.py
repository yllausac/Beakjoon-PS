hobit = []
for i in range(9):
    hobit.append(int(input()))
one = 0
two = 0
for i in range(8):
    for j in range(i+1, 9):
        if sum(hobit) - (hobit[i] + hobit[j]) == 100:
            one = hobit[i]
            two = hobit[j]
hobit.remove(one)
hobit.remove(two)
hobit.sort()
for i in hobit:
    print(i)

