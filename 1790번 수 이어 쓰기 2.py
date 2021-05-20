n, k = map(int, input().split())

total_num = 0
num_count = 9
num_length = 1
tenten = 1
cal_k = k
result = -1

while cal_k > num_count * num_length:
    total_num += num_count
    cal_k -= num_count * num_length
    num_count *= 10
    num_length += 1

total_num += (cal_k - 1) // num_length + 1

if total_num > n:
    print(result)
    exit()
else:
    temp = (cal_k - 1) % num_length + 1

    for i in range(num_length - 1):
        tenten *= 10

    for j in range(temp):
        result = total_num // tenten
        total_num %= tenten
        tenten //= 10

print(result)
