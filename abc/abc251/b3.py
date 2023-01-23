N, W = map(int, input().split())
a = list(map(int, input().split()))

s = set()
for i in range(N):
    s.add(a[i])
    for j in range(i+1, N):
        s.add(a[i] + a[j])
        for k in range(j+1, N):
            s.add(a[i] + a[j] + a[k])

nums = list(filter(lambda v: v <= W, s))
print(len(nums))