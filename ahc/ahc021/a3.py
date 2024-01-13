import sys
import math


def ndan(hoge):
    return hoge * (hoge + 1) // 2


def check(n, dan):
    d1 = ndan(dan + 1) - 1
    d2 = ndan(dan) - 1

    hantei = d2 < n and n <= d1

    return hantei


def solve_dan(n):
    return (-1 + math.sqrt(n * 8 + 1)) / 2


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
        if check(n, y):
            break

        if x == 0:
            x2 = 0
        elif x == y:
            x2 = x - 1
        else:
            kouho1 = b[y-1][x - 1]
            kouho2 = b[y-1][x]

            k_d1 = solve_dan(kouho1)
            k_d2 = solve_dan(kouho2)
            diff1 = k_d1 - (y - 1)
            diff2 = k_d2 - (y - 1)

            x2 = x - 1 if diff1 > diff2 else x

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
