import math

N = int(input())
a = list(map(int, input().split()))
X = int(input())

N_sum = sum(a)
count = math.floor(X / N_sum) * N
num_sum = math.floor(X / N_sum) * N_sum

if num_sum > X:
    print(count)
    exit(0)

for v in a:
    num_sum += v
    count += 1
    if num_sum > X:
        print(count)
        break
