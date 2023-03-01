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
    return min(c * (2 ** count), maxPower)


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

    if w == -1 or h == -1:
        break

    # 水源から家まで掘り進む、とりあえずx座標 ⇨ y座標の順番
    # HACK: 家が間にあったらそこを通るようにしたらいいかも
    wx, wy = w
    hx, hy = h
    if wx > hx:
        wx, hx = hx, wx

    for i in range(wx, hx + 1):
        count = 0
        total = 0
        while True:
            power = min(calcPower(C, count), 5000 - total)
            total += power
            if attack(destroyed, i, wy, power):
                break

            count += 1

        waters.append((i, wy))
        
    wx, wy = w
    hx, hy = h
    if wy > hy:
        wy, hy = hy, wy
    
    for i in range(wy, hy + 1):
        count = 0
        total = 0
        while True:
            power = min(calcPower(C, count), 5000 - total)
            total += power
            if attack(destroyed, hx, i, power):
                break

            count += 1

        waters.append((hx, i))