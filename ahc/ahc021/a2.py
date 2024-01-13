import sys


def ndan(hoge):
    return hoge * (hoge + 1) // 2


def check(n, dan):
    d1 = ndan(dan + 1) - 1
    d2 = ndan(dan) - 1

    hantei = d2 < n and n <= d1

    # print('dan', dan)
    # print('n d1 d2', n, d1, d2)
    # print('hantei', hantei)

    return hantei


def output(opes):
    print(len(opes))
    print('\n'.join(opes))


def exchange(b_ope, b, n):
    xy = -1, -1
    for i, row in enumerate(b):
        for j, v in enumerate(row):
            if v == n:
                xy = j, i
                break

        if xy != (-1, -1):
            break

    opes = []
    while True:
        x, y = xy
        # print('nxy', n, x, y)
        if check(n, y):
            break

        d2 = ndan(y)
        is_left = x != 0

        if x != y and check(b[y - 1][x - 1], y-1):
            is_left = False

        if x == y + 1:
            is_left = True

        x2 = (x - 1) if is_left else x
        y2 = y - 1

        # 動かしている数字より小さい数字は動かさない
        if b[y2][x2] < n:
            diff = 1000
            index = -1
            for i, v in enumerate(b[y2]):
                if v > n:
                    if i < x:
                        n_diff = abs(i - 1 - x)
                    else:
                        n_diff = abs(x - i)

                    if diff > n_diff:
                        index = i
                        diff = n_diff

            while index + 1 != x and index != x:
                if index > x:
                    ope = ' '.join(list(map(str, list((y, x, y, x + 1)))))
                    b[y][x], b[y][x+1] = b[y][x+1], b[y][x]
                    x += 1
                else:
                    ope = ' '.join(list(map(str, list((y, x, y, x - 1)))))
                    b[y][x], b[y][x-1] = b[y][x-1], b[y][x]
                    x -= 1

                opes.append(ope)

            x2 = index

        b[y][x], b[y2][x2] = b[y2][x2], b[y][x]

        ope = ' '.join(list(map(str, list((y, x, y2, x2)))))

        xy = x2, y2
        opes.append(ope)

    return opes


b = []
count = 0
for _ in range(30):
    v = list(map(int, input().split()))
    count += len(v)
    b.append(v)

opes = []
for n in range(count):
    opes.extend(exchange(opes, b, n))

output(opes)
