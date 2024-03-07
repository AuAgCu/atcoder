D, N = map(int, input().split())

arr = [24] * D
for i in range(N):
    l, r, h = map(int, input().split())

    l -= 1
    r -= 1
    for j in range(l, r + 1):
        arr[j] = min(arr[j], h)

print(sum(arr))