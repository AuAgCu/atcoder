N, W = map(int, input().split())
a = list(map(int, input().split()))

w_arr = [False for i in range(W+1)]

for i in range(N):
    
    if a[i] < len(w_arr):
        w_arr[a[i]] = True
    
    for j in range(i+1, N):

        if a[i] + a[j] < len(w_arr):
            w_arr[a[i] + a[j]] = True

        for k in range(j+1, N):
            if a[i] + a[j] + a[k] < len(w_arr):
                w_arr[a[i] + a[j] + a[k]] = True

print(w_arr[:W+1].count(True))