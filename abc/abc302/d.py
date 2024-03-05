import bisect
N, M, D = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()

diff = -1

for v in a:
    i1 = bisect.bisect_left(b, v - D)
    i2 = bisect.bisect_right(b, v + D)

    if i1 < M - 1:
        if abs(v - b[i1]) > D:
            continue

        diff = max(diff, b[i1] + v)

    if i2 > 0:
        if abs(v - b[i2 - 1]) > D:
            continue

        diff = max(diff, b[i2 - 1] + v)

print(diff)