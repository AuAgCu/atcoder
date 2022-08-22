N, W = map(int, input().split())
a = list(map(int, input().split()))

w_arr = [False for i in range((10**6) * 3 + 1)]

for i in range(N):
    w_arr[a[i]] = True
    for j in range(i+1, N):
        w_arr[a[i] + a[j]] = True
        for k in range(j+1, N):
            w_arr[a[i] + a[j] + a[k]] = True

print(w_arr[:W+1].count(True))