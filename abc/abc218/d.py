N = int(input())
MAX = 10 ** 9 + 1

array_y = {}
array_x = {}
dots = []
for _ in range(N):
    x, y = map(int, input().split())
    array_x.setdefault(x, set())
    array_y.setdefault(y, set())
    array_x[x].add(y)
    array_y[y].add(x)

    dots.append((x, y))

count = 0
for i in range(N):
    for j in range(i+1, N):
        x1, y1 = dots[i]
        x2, y2 = dots[j]
        if x1 == x2 or y1 == y2:
            continue

        if y2 in array_x[x1] and x2 in array_y[y1]:
            count += 1

print(count // 2)
