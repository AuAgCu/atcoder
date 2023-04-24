_ = int(input())
a = list(map(int, input().split()))

R = 200
dict = {}
for v in a:
    mod = v % R
    dict.setdefault(mod, 0)
    dict[mod] += 1

ans = 0
for (i, v) in dict.items():
    if v <= 1:
        continue

    ans += v * (v-1) // 2

print(ans)
