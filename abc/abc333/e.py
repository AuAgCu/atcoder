N = int(input())

history = []
potion = {}
potion_position = []
for i in range(N):
    t, x = map(int, input().split())
    if t == 1:
        potion.setdefault(x, [])
        potion[x].append(i)
        potion_position.append(i)
    else:
        if potion.get(x, 0) == 0:
            print(-1)
            exit(0)

        position_x = potion[x].pop()
        history.append((i, -1))
        history.append((position_x, 1))

history.sort()

m = 0
p = 0
arr = set()
for v in history:
    d, diff = v
    p += diff
    m = max(m, p)

    arr.add(d)

print(m)
for v in potion_position:
    if v in arr:
        print(1, end=' ')
    else:
        print(0, end=' ')

print()