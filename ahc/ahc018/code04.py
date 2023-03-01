import sys
import math
def attack(destroyed, x, y, power):
    if destroyed[x][y]:
        return True
    
    print(x, y, power)
    result = int(input())

    if result == -1 or result == 2:
        exit(0)

    # 壊れたらTrue, 壊れなかったらFalse
    if result == 1:
        destroyed[x][y] = True
        return True
    else:
        return False

def calcPower(c, count):
    # 攻撃回数による損失と、powerが高すぎた時の損失値が同じくらいになるようにした値
    maxPower = math.ceil(math.sqrt(5000 * c))

    # 最初の値を小さくして、大きすぎる攻撃による損失を防ぐ
    return min(c * (2 ** count), maxPower)

def straightX(waters, destroyed, x, y1, y2):
    if y1 > y2:
        y1, y2 = y2, y1

    for i in range(y1, y2 + 1):
        count = 0
        total = 0
        while True:
            power = min(calcPower(C, count), 5000 - total)
            total += power
            if attack(destroyed, x, i, power):
                break

            count += 1

        waters.append((x, i))
        destroyed[x][i]

def straightY(waters, destroyed, y, x1, x2):
    if x1 > x2:
        x1, x2 = x2, x1

    for i in range(x1, x2 + 1):
        count = 0
        total = 0
        while True:
            power = min(calcPower(C, count), 5000 - total)
            total += power
            if attack(destroyed, i, y, power):
                break

            count += 1

        waters.append((i, y))
        destroyed[i][y]

def tunnel(waters, destroyed, houses, x1, y1, x2, y2):
    # 水源から家まで掘り進む、とりあえずx座標 ⇨ y座標の順番
    # HACK: 家が間にあったらそこを通るようにしたらいいかも
    
    if x1 == x2:
        straightX(waters, destroyed, x1, y1, y2)
        return

    if y1 == y2:
        straightY(waters, destroyed, y1, x1, x2)
        return

    first = (x1 < x2 and y1 < y2) or (x1 > x2 and y1 > y2)

    if x1 > x2:
        x1, x2 = x2, x1
    
    if y1 > y2:
        y1, y2 = y2, y1
        
    # 左下から右上に行く場合、右⇨上 or 上⇨右でルートが変わるので、まだ水が通ってない家が多い方を選ぶ
    if first:
        rightBottom = (x2, y1)
        leftTop = (x1, y2)

        rightBottomCount = 0
        for i in range(0, rightBottom[0] + 1):
            for j in range(rightBottom[1], N):
                for house in houses:
                    if house[0] == i and house[1] == j and not destroyed[i][j]:
                        rightBottomCount += 1

        leftTopCount = 0
        for i in range(leftTop[0], N):
            for j in range(0, leftTop[1] + 1):
                for house in houses:
                    if house[0] == i and house[1] == j and not destroyed[i][j]:
                        leftTopCount += 1

        if rightBottomCount > leftTopCount:
            print('#左上')
            straightX(waters, destroyed, x1, y1, y2)
            straightY(waters, destroyed, y2, x1, x2)
        else:
            print('#右下')
            straightY(waters, destroyed, y1, x1, x2)
            straightX(waters, destroyed, x2, y1, y2)

    # 右下から左上に行く場合、ルートが変わるので、まだ水が通ってない家が多い方を選ぶ
    else:
        leftBottom = (x1, y1)
        rightTop = (x2, y2)

        leftBottomCount = 0
        for i in range(leftBottom[0], N):
            for j in range(leftBottom[1], N):
                for house in houses:
                    if house[0] == i and house[1] == j and not destroyed[i][j]:
                        leftBottomCount += 1

        rightTopCount = 0
        for i in range(0, rightTop[0] + 1):
            for j in range(0, rightTop[1] + 1):
                for house in houses:
                    if house[0] == i and house[1] == j and not destroyed[i][j]:
                        rightTopCount += 1

        if leftBottomCount < rightTopCount:
            print('#左下')
            straightY(waters, destroyed, y1, x1, x2)
            straightX(waters, destroyed, x1, y1, y2)
        else:
            print('#右上')
            straightX(waters, destroyed, x2, y1, y2)
            straightY(waters, destroyed, y2, x1, x2)
            

N, W, K, C = map(int, input().split())
destroyed = [[False for _ in range(N)] for _ in range(N)]

waters = []
for _ in range(W):
    a, b = map(int, input().split())
    waters.append((a, b))

houses =[]
for _ in range(K):
    c, d = map(int, input().split())
    houses.append((c, d))

while True:
    # 一番距離が近い家と水源（水が流れてるところも含む）のペアを探す
    diff = sys.maxsize
    w, h = -1, -1
    for water in waters:
        w_x, w_y = water
        for house in houses:
            h_x, h_y = house
            if destroyed[h_x][h_y]:
                continue

            distance = abs(w_x - h_x) + abs(w_y - h_y)
            if diff > distance:
                diff = distance
                w, h = water, house

    wx, wy = w
    hx, hy = h
    tunnel(waters, destroyed, houses, wx, wy, hx, hy)