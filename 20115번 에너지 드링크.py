N = int(input())
X = list(map(int, input().split()))
X.sort(reverse = True)
print(X)
drink = X[0]


for i in range(1, len(X)):
    drink += (X[i]/2)
if drink == int(drink):
    print(int(drink))
else:
    print(drink)